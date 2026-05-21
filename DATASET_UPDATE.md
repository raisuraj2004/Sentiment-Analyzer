# 📊 Dataset Update - train_data.csv

## Changes Made

The Tweet Sentiment Analyzer project has been updated to use your provided `train_data.csv` dataset instead of the original Sentiment140 dataset plan.

### Dataset Details

**File:** `train_data.csv`
**Location:** Parent directory (same level as SentiAnalyzer folder)
**Size:** ~98 MB
**Format:** CSV with headers

### Column Structure

```
sentence,sentiment
```

- **Column 1: `sentence`** - Text data (pre-processed)
- **Column 2: `sentiment`** - Labels (0=negative, 1=positive)

### Example Data

```
sentence,sentiment
awww that s a bummer you shoulda got david carr of third day to do it d,0
is upset that he can t update his facebook by texting it and might cry as a result school today also blah,0
i dived many times for the ball managed to save the rest go out of bounds,0
my whole body feels itchy and like its on fire,0
...
```

---

## Updated Files

### 1. **train.py** ✅
- Changed dataset loading from Sentiment140 format to train_data.csv
- Updated column mapping: `['sentence', 'sentiment']` → `['text', 'target']`
- Dataset path: `../train_data.csv`
- Removed Sentiment140-specific transformations

### 2. **evaluate.py** ✅
- Changed dataset loading to use train_data.csv
- Updated column mapping to match train.py
- Dataset path: `../train_data.csv`

### 3. **README.md** ✅
- Updated Setup Instructions to reference train_data.csv
- Updated Dataset Credit section
- Updated Folder Structure diagram
- Updated Model Details section
- Updated performance expectations

### 4. **SETUP_GUIDE.md** ✅
- Step 2: Changed from "Download from Kaggle" to "Place provided dataset"
- Updated dataset info section
- Reduced estimated training time: 30-60 mins → 2-5 minutes
- Updated expected output example

### 5. **QUICKSTART.md** ✅
- Step 2: Changed to reference provided dataset
- Updated training time estimate

### 6. **.gitignore** ✅
- Commented out `data/` folder exclusion
- Now excludes only model/*.pkl files

---

## Usage Instructions

### Before Training

1. Ensure `train_data.csv` is in the parent directory
2. The project is at: `C:\Users\raisu\OneDrive\Desktop\SentiAnalyzer`
3. The dataset should be at: `C:\Users\raisu\OneDrive\Desktop\train_data.csv`

### Directory Structure

```
Desktop/
├── SentiAnalyzer/
│   ├── app.py
│   ├── train.py
│   ├── evaluate.py
│   ├── streamlit_app.py
│   └── preprocessing.py
└── train_data.csv  ← Place dataset here
```

### Training Command

```bash
cd C:\Users\raisu\OneDrive\Desktop\SentiAnalyzer
python train.py
```

The script will:
1. Read `../train_data.csv`
2. Clean and preprocess text
3. Split into 80/20 train/test
4. Train LogisticRegression model
5. Save to `model/model.pkl` and `model/vectorizer.pkl`
6. Display metrics

---

## Performance Expectations

With the provided dataset:

- **Training Time:** 2-5 minutes (vs 30-60 min with Sentiment140)
- **Expected Accuracy:** ~80-85%
- **Model Size:** Depends on dataset size

### Metrics Output

```
Accuracy: 0.82XX
Classification Report:
              precision    recall  f1-score   support
    Negative       0.82      0.82      0.82    XXXXX
    Positive       0.82      0.82      0.82    XXXXX
    accuracy                           0.82    XXXXX
```

---

## What Didn't Change

✅ Preprocessing pipeline (still 8 steps)
✅ Flask API endpoints (/health, /predict)
✅ Streamlit web UI
✅ Model algorithm (LogisticRegression)
✅ Vectorizer (TF-IDF with bigrams)
✅ All other code quality standards

---

## Quick Start (Updated)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Place train_data.csv in parent directory
# Already done: C:\Users\raisu\OneDrive\Desktop\train_data.csv

# 3. Train model (2-5 minutes)
python train.py

# 4. Run Flask API
python app.py

# 5. Run Streamlit UI (new terminal)
streamlit run streamlit_app.py

# 6. Open browser
# http://localhost:8501
```

---

## Verification

After updating, you can verify everything is working:

```bash
# Check preprocessing
python -c "from preprocessing import clean_text; print(clean_text('Hello, World!'))"

# Check model training
python train.py  # Should load from ../train_data.csv

# Check evaluation
python evaluate.py  # Should use the trained model
```

---

## Summary

✅ All scripts updated to use train_data.csv
✅ Documentation updated
✅ Training time significantly reduced
✅ No functional changes to the ML pipeline
✅ Ready to train and deploy!

**Status:** Ready for training

---

*Update Date: 2026-05-21*
*Dataset: train_data.csv (98 MB)*
*Project Status: ✅ Updated & Ready*
