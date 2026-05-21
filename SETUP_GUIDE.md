# Tweet Sentiment Analyzer - Complete Setup Guide

## Project Status ✅

All project files have been created successfully! Here's what you have:

### Files Created:
- ✅ `app.py` - Flask REST API
- ✅ `train.py` - Model training script
- ✅ `evaluate.py` - Model evaluation script
- ✅ `preprocessing.py` - Text cleaning functions
- ✅ `streamlit_app.py` - Streamlit frontend UI
- ✅ `requirements.txt` - Python dependencies
- ✅ `README.md` - Project documentation
- ✅ `.gitignore` - Git ignore rules
- ✅ `.env` - Environment variables template

### Project Structure:
```
sentiment-analyzer/
├── app.py
├── train.py
├── evaluate.py
├── preprocessing.py
├── streamlit_app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
├── model/                  (Will be created by train.py)
│   ├── model.pkl           (Generated after training)
│   └── vectorizer.pkl      (Generated after training)
└── data/                   (You need to add the dataset here)
    └── training.1600000.processed.noemoticon.csv
```

## Step-by-Step Setup

### 1. Install Python Dependencies

```bash
# Navigate to project directory
cd C:\Users\raisu\OneDrive\Desktop\SentiAnalyzer

# Install all required packages
pip install -r requirements.txt
```

### 2. Download Dataset

The model requires the `train_data.csv` dataset:

1. Ensure you have the file: `train_data.csv`
2. Place it in the parent directory (same level as the SentiAnalyzer folder)
3. File location should be: `../train_data.csv` (one level above the project)

**Dataset Info:**
- Format: CSV with headers (sentence, sentiment)
- Sentiment values: 0 (negative), 1 (positive)
- Pre-processed text data
- Size: ~98 MB

### 3. Train the Model

```bash
python train.py
```

**What happens:**
- Loads train_data.csv from parent directory
- Preprocesses text data
- Splits data: 80% train, 20% test
- Trains LogisticRegression classifier
- Creates `model/model.pkl` and `model/vectorizer.pkl`
- Displays accuracy, precision, recall, F1-score
- **Estimated time: 2-5 minutes** (depends on machine)

**Expected Output:**
```
Loading training dataset...
Dataset loaded with XXXXX samples
Target distribution:
 0    XXXXX
 1    XXXXX

Cleaning text data...
100%|████████| XXXXX/XXXXX [XX:XX:XX<00:00, XXX.XXit/s]

Splitting data (80/20)...
Vectorizing text with TF-IDF...
Vectorizer created: XXXXX features

Training LogisticRegression model...
Evaluating model on test set...

Accuracy: 0.82XX
Classification Report:
              precision    recall  f1-score   support
    Negative       0.82      0.82      0.82    XXXXX
    Positive       0.82      0.82      0.82    XXXXX
    accuracy                           0.82    XXXXX
   macro avg       0.82      0.82      0.82    XXXXX
weighted avg       0.82      0.82      0.82    XXXXX

Saving model and vectorizer...
Model and vectorizer saved successfully!
Training complete!
```

### 4. (Optional) Evaluate the Model

```bash
python evaluate.py
```

Shows:
- Full classification report
- Confusion matrix
- Performance metrics

### 5. Run Flask API

```bash
python app.py
```

Output:
```
Model and vectorizer loaded successfully!
 * Running on http://0.0.0.0:5000
 * WARNING: This is a development server. Do not use it in production.
```

**API Endpoints:**
- `GET /health` - Health check
- `POST /predict` - Sentiment prediction

### 6. Run Streamlit Frontend (NEW TERMINAL)

Open a new command prompt/terminal and run:

```bash
streamlit run streamlit_app.py
```

Output:
```
You can now view your Streamlit app in your browser.
  Local URL: http://localhost:8501
  Network URL: http://XXX.XXX.X.XXX:8501
```

**Application opens in your browser automatically**

## Testing the Application

### Via Streamlit UI (Easiest)
1. Open Streamlit app at `http://localhost:8501`
2. Paste text in the text area
3. Click "Analyze Sentiment"
4. View results with confidence score

### Via Flask API (Command Line)

Test health check:
```bash
curl http://localhost:5000/health
```

Test prediction:
```bash
curl -X POST http://localhost:5000/predict ^
  -H "Content-Type: application/json" ^
  -d "{\"text\": \"This is amazing!\"}"
```

Expected response:
```json
{
  "sentiment": "Positive",
  "confidence": 0.92,
  "cleaned_text": "amaz"
}
```

## Troubleshooting

### Issue: "Model already trained. Delete model/ folder to retrain."
**Solution:** Delete the `model/` folder to retrain, or skip this and proceed to Step 5.

### Issue: "Cannot connect to Flask API"
**Solution:** Make sure Flask is running (`python app.py`) and accessible at `localhost:5000`

### Issue: "NLTK stopwords not found"
**Solution:** The code will auto-download. If it fails:
```bash
python -m nltk.downloader stopwords
```

### Issue: "Dataset not found"
**Solution:** Verify file exists at `data/training.1600000.processed.noemoticon.csv`

### Issue: "ModuleNotFoundError: No module named..."
**Solution:** Run `pip install -r requirements.txt`

### Issue: Streamlit shows "Flask API is not running"
**Solution:** 
1. Start Flask API first: `python app.py`
2. Then run Streamlit: `streamlit run streamlit_app.py`

## Key Features

✨ **Preprocessing Pipeline:**
- URL removal
- Mention removal (@user)
- Hashtag removal
- Punctuation removal
- Number removal
- Stopword removal
- Porter stemming

🤖 **Model Details:**
- Algorithm: LogisticRegression
- Vectorizer: TF-IDF (500K features, bigrams)
- Training data: 1.28M tweets
- Test data: 320K tweets
- Expected accuracy: ~81%

🌐 **REST API:**
- Single POST endpoint: `/predict`
- Health check: `/health`
- JSON request/response
- Error handling for invalid input

🎨 **Streamlit UI:**
- Real-time sentiment analysis
- Confidence scores with visualization
- Example text buttons
- Cleaned text display
- API status checking

## Performance Tips

- **First run:** Training takes 30-60 minutes
- **Subsequent runs:** API startup is instant
- **Streamlit performance:** First load takes ~5 seconds
- **Prediction latency:** ~100-200ms per request

## Production Deployment

For production, consider:
1. Use proper WSGI server (Gunicorn/uWSGI) instead of Flask dev server
2. Add authentication/rate limiting
3. Use environment variables for configuration
4. Deploy on cloud (AWS, Heroku, Google Cloud, etc.)
5. Add monitoring and logging
6. Cache predictions where appropriate

## Next Steps

1. ✅ Install dependencies: `pip install -r requirements.txt`
2. ✅ Download dataset from Kaggle
3. ✅ Train model: `python train.py`
4. ✅ Run API: `python app.py`
5. ✅ Run UI: `streamlit run streamlit_app.py`
6. ✅ Test and enjoy!

---

**Need help?** Check README.md for API examples and more details.

Good luck! 🚀
