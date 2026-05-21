"""
Streamlit frontend UI for Tweet Sentiment Analyzer.
Provides an interactive interface to analyze sentiment of text.
"""
import streamlit as st
import requests
import json

st.set_page_config(page_title="Tweet Sentiment Analyzer", layout="wide")

# Title and subtitle
st.title("Tweet Sentiment Analyzer")
st.markdown("Paste any tweet or product review to analyze its sentiment")

# Constants
API_URL = "http://localhost:5000/predict"
HEALTH_CHECK_URL = "http://localhost:5000/health"


def check_api_running():
    """
    Check if Flask API is running.
    
    Returns:
        bool: True if API is running, False otherwise
    """
    try:
        response = requests.get(HEALTH_CHECK_URL, timeout=2)
        return response.status_code == 200
    except:
        return False


def call_api(text):
    """
    Call Flask API to predict sentiment.
    
    Args:
        text (str): Text to analyze
        
    Returns:
        dict: API response or None if error
    """
    try:
        response = requests.post(
            API_URL,
            json={"text": text},
            timeout=10
        )
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"API Error: {response.json().get('error', 'Unknown error')}")
            return None
    except requests.exceptions.ConnectionError:
        st.error(" Cannot connect to Flask API. Please make sure it's running on localhost:5000")
        return None
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None


# Check if API is running
api_running = check_api_running()
if not api_running:
    st.warning(
        "Flask API is not running! Please start it with: `python app.py`"
    )

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Enter Text to Analyze")
    user_text = st.text_area(
        "Paste a tweet or product review here:",
        height=150,
        placeholder="Enter your text here...",
        label_visibility="collapsed"
    )

with col2:
    st.subheader("Example Texts")
    
    positive_example = "I absolutely love this product! It's amazing and works perfectly. Highly recommended!"
    negative_example = "This is the worst experience ever. Terrible quality and horrible customer service. Very disappointed."
    
    if st.button("Positive Example", use_container_width=True):
        user_text = positive_example
        st.session_state['example_text'] = positive_example
    
    if st.button("Negative Example", use_container_width=True):
        user_text = negative_example
        st.session_state['example_text'] = negative_example

# Load example from session state if set
if 'example_text' in st.session_state:
    user_text = st.session_state['example_text']

# Analyze button
if st.button(" Analyze Sentiment", use_container_width=True, disabled=not api_running):
    if not user_text.strip():
        st.warning("Please enter some text to analyze!")
    else:
        with st.spinner("Analyzing..."):
            result = call_api(user_text)
        
        if result:
            sentiment = result['sentiment']
            confidence = result['confidence']
            cleaned_text = result['cleaned_text']
            confidence_percentage = confidence * 100
            
            # Display result based on sentiment
            if sentiment == "Positive":
                st.success(
                    f" **POSITIVE SENTIMENT** - Confidence: **{confidence_percentage:.1f}%**"
                )
            else:
                st.error(
                    f" **NEGATIVE SENTIMENT** - Confidence: **{confidence_percentage:.1f}%**"
                )
            
            # Show cleaned text in expander
            with st.expander(" View Cleaned Text"):
                st.text(cleaned_text)
            
            # Show confidence bar chart
            st.subheader("Confidence Score")
            chart_data = {
                "Sentiment": [sentiment],
                "Confidence": [confidence_percentage]
            }
            st.bar_chart(
                {"Confidence": [confidence_percentage]},
                height=300
            )

# Footer
st.divider()
st.markdown(
    """
    <div style='text-align: center; color: gray; font-size: 12px;'>
    <p>Tweet Sentiment Analyzer | Built with Streamlit, Flask & Scikit-learn</p>
    </div>
    """,
    unsafe_allow_html=True
)
