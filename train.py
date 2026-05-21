"""
Model training script for sentiment analysis.
Trains a LogisticRegression model on the provided train_data.csv dataset.
"""
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import joblib
from tqdm import tqdm
from preprocessing import clean_text

# Set tqdm to work with pandas
tqdm.pandas()


def train_model():
    """
    Train sentiment analysis model on provided training dataset.
    """
    # Check if model already exists
    if os.path.exists('model/model.pkl'):
        print("Model already trained. Delete model/ folder to retrain.")
        return
    
    print("Loading training dataset...")
    # Load dataset - the dataset has 'sentence' and 'sentiment' columns
    df = pd.read_csv(
        '../train_data.csv'
    )
    
    # Rename columns for consistency with preprocessing
    df.columns = ['text', 'target']
    
    print(f"Dataset loaded with {len(df)} samples")
    print(f"Target distribution:\n{df['target'].value_counts()}")
    
    # Clean text with progress bar
    print("\nCleaning text data...")
    df['cleaned_text'] = df['text'].progress_apply(clean_text)
    
    # Split data: 80% train, 20% test
    print("\nSplitting data (80/20)...")
    X_train, X_test, y_train, y_test = train_test_split(
        df['cleaned_text'],
        df['target'],
        test_size=0.2,
        random_state=42,
        stratify=df['target']
    )
    
    # Vectorize text with TF-IDF
    print("\nVectorizing text with TF-IDF...")
    vectorizer = TfidfVectorizer(max_features=500000, ngram_range=(1, 2))
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)
    
    print(f"Vectorizer created: {X_train_vec.shape[1]} features")
    
    # Train LogisticRegression model
    print("\nTraining LogisticRegression model...")
    model = LogisticRegression(max_iter=1000, C=1.0, solver='lbfgs')
    model.fit(X_train_vec, y_train)
    
    # Evaluate on test set
    print("\nEvaluating model on test set...")
    y_pred = model.predict(X_test_vec)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\nAccuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=['Negative', 'Positive']))
    
    # Save model and vectorizer
    print("\nSaving model and vectorizer...")
    os.makedirs('model', exist_ok=True)
    joblib.dump(model, 'model/model.pkl')
    joblib.dump(vectorizer, 'model/vectorizer.pkl')
    
    print("Model and vectorizer saved successfully!")
    print("Training complete!")


if __name__ == '__main__':
    train_model()
