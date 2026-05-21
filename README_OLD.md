# Tweet Sentiment Analyzer

> A machine learning web app that classifies tweets and product reviews as Positive or Negative with confidence scores.

## Tech Stack

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-black?logo=flask&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-red?logo=streamlit&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0%2B-orange?logo=scikit-learn&logoColor=white)

## How It Works

- **Text Preprocessing**: Cleans input text by removing URLs, mentions, hashtags, punctuation, stopwords, and applying stemming
- **Feature Extraction**: Uses TF-IDF vectorization with up to 500K features and bigrams for rich text representation
- **Model Training**: Trains a LogisticRegression classifier on 1.6M tweets from the Sentiment140 dataset
- **REST API**: Exposes a Flask API endpoint for sentiment predictions with confidence scores
- **Interactive UI**: Provides a Streamlit frontend with real-time sentiment analysis and visualization

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Training dataset: `train_data.csv`

### 1. Clone the Repository
```bash
git clone <repository-url>
cd sentiment-analyzer
```

### 2. Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Place Training Dataset
Place the `train_data.csv` dataset in the parent directory:
- File: `train_data.csv`
- Location: One level above the project (same as SentiAnalyzer folder)

**Dataset Structure:**
```
train_data.csv  (one level above SentiAnalyzer/)
```

The CSV has headers: `sentence,sentiment`
- Column 1: sentence (text data)
- Column 2: sentiment (0=negative, 1=positive)

### 5. Train the Model
```bash
python train.py
```

This will:
- Load and preprocess 1.6M tweets
- Split data (80% train, 20% test)
- Train a LogisticRegression model
- Save model and vectorizer to `model/` folder
- Display evaluation metrics

**Note**: First run takes ~30-60 minutes depending on hardware. Subsequent runs will skip training if model exists.

### 6. Run Flask API
```bash
python app.py
```

The API will start on `http://localhost:5000`

### 7. Run Streamlit Frontend (in another terminal)
```bash
streamlit run streamlit_app.py
```

The UI will open at `http://localhost:8501`

## API Usage

### Health Check
```bash
curl http://localhost:5000/health
```

Response:
```json
{"status": "ok"}
```

### Predict Sentiment
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "I absolutely love this product!"}'
```

Response:
```json
{
  "sentiment": "Positive",
  "confidence": 0.92,
  "cleaned_text": "absolut love product"
}
```

## Folder Structure
```
sentiment-analyzer/
├── app.py                  # Flask REST API
├── train.py                # Model training script
├── evaluate.py             # Model evaluation script
├── preprocessing.py        # Text cleaning functions
├── streamlit_app.py        # Streamlit frontend UI
├── requirements.txt        # Python dependencies
├── README.md               # This file
├── .gitignore              # Git ignore rules
├── model/
│   ├── model.pkl           # Trained LogisticRegression model
│   └── vectorizer.pkl      # TF-IDF vectorizer
└── ../train_data.csv       # Training dataset (parent directory)
```

## Model Details

- **Algorithm**: LogisticRegression (max_iter=1000, C=1.0, solver='lbfgs')
- **Vectorizer**: TfidfVectorizer (max_features=500K, bigrams)
- **Dataset**: Provided train_data.csv
- **Train/Test Split**: 80/20 with stratification
- **Preprocessing**: NLTK stopwords removal, Porter stemming

## Dataset Credit

Dataset: Provided `train_data.csv`
- CSV format with headers: sentence, sentiment
- Binary classification: 0 (negative), 1 (positive)
- Pre-processed text data

## Example

**Input:**
```
"This movie was absolutely fantastic! Best film I've seen in years!"
```

**Output:**
```json
{
  "sentiment": "Positive",
  "confidence": 0.95,
  "cleaned_text": "fantast best film seen year"
}
```

## Performance

On provided test set (20% of training data):
- **Accuracy**: ~80-85%
- **Precision**: ~80-85%
- **Recall**: ~80-85%
- **F1-Score**: ~80-85%

*(Exact metrics depend on dataset split and random seed)*

## License

MIT License - See LICENSE file for details

## Support

For issues, questions, or contributions, please open an issue or contact the maintainers.
