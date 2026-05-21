"""
Model evaluation script for sentiment analysis.
Evaluates the trained model on test data.
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import joblib
from preprocessing import clean_text


def evaluate_model():
    """
    Evaluate sentiment analysis model on test set.
    """
    print("Loading model and vectorizer...")
    model = joblib.load('model/model.pkl')
    vectorizer = joblib.load('model/vectorizer.pkl')
    
    print("Loading and preparing test data...")
    # Load dataset
    df = pd.read_csv(
        '../train_data.csv'
    )
    
    # Rename columns for consistency
    df.columns = ['text', 'target']
    
    # Clean text
    df['cleaned_text'] = df['text'].apply(clean_text)
    
    # Split data with same random_state=42
    X_train, X_test, y_train, y_test = train_test_split(
        df['cleaned_text'],
        df['target'],
        test_size=0.2,
        random_state=42,
        stratify=df['target']
    )
    
    # Vectorize test data
    X_test_vec = vectorizer.transform(X_test)
    
    # Make predictions
    y_pred = model.predict(X_test_vec)
    
    # Print evaluation results
    print("\n" + "="*50)
    print("CLASSIFICATION REPORT")
    print("="*50)
    print(classification_report(y_test, y_pred, target_names=['Negative', 'Positive']))
    
    print("\n" + "="*50)
    print("CONFUSION MATRIX")
    print("="*50)
    cm = confusion_matrix(y_test, y_pred)
    print(f"True Negatives: {cm[0][0]}")
    print(f"False Positives: {cm[0][1]}")
    print(f"False Negatives: {cm[1][0]}")
    print(f"True Positives: {cm[1][1]}")
    print(f"\nConfusion Matrix:\n{cm}")


if __name__ == '__main__':
    evaluate_model()
