# 🎯 SentiAnalyzer

**Professional Sentiment Analysis Platform with Machine Learning**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-black?logo=flask)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0%2B-orange)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

SentiAnalyzer is an intelligent sentiment analysis tool that uses advanced machine learning to classify text as positive or negative with confidence scores. It features a professional web interface with real-time analytics, history tracking, and interactive charts.

## ✨ Features

- 🎯 **Real-time Sentiment Analysis** - Classify text as Positive or Negative instantly
- 📊 **Confidence Scores** - Get probability scores (0-100%) for prediction reliability
- 📈 **Interactive Analytics** - Track sentiment trends with dynamic charts
- 💾 **History Tracking** - Persistent analysis history with browser LocalStorage
- 📱 **Responsive Design** - Works seamlessly on desktop, tablet, and mobile
- 🎨 **Modern UI/UX** - Professional interface with smooth animations
- ⚡ **Fast Processing** - Optimized ML pipeline for quick predictions
- 🔒 **Secure** - Client-side data storage, no external data transmission

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/SentiAnalyzer.git
cd SentiAnalyzer
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Train the model** (if not already trained)
```bash
python train.py
```

4. **Run the application**
```bash
python app.py
```

5. **Open in browser**
```
http://localhost:5000
```

## 📚 How It Works

### Architecture

```
User Input (Text)
       ↓
Preprocessing (NLTK)
  - Tokenization
  - Lowercasing
  - Punctuation removal
  - Stop word handling
       ↓
Vectorization (TF-IDF)
  - Convert text to numerical features
  - Dimensionality reduction
       ↓
ML Classifier (scikit-learn)
  - Logistic Regression / SVM
  - Probability calculation
       ↓
Sentiment Output
  - Classification (Positive/Negative)
  - Confidence Score (0-100%)
  - Cleaned Text
```

### Process Flow

1. **Input** - User enters text in the web interface
2. **Cleaning** - Text is preprocessed using NLTK
   - Convert to lowercase
   - Remove punctuation and special characters
   - Tokenize into words
   - Remove stop words (the, a, an, etc.)
3. **Vectorization** - TF-IDF converts words to numerical features
4. **Prediction** - Trained ML model classifies sentiment
5. **Results** - Display sentiment, confidence, and history
6. **Analytics** - Update charts with new data

## 🔧 Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Frontend** | HTML5, CSS3, Vanilla JavaScript | Modern responsive UI |
| **Backend** | Flask (Python) | REST API server |
| **Machine Learning** | scikit-learn | Model training & prediction |
| **NLP** | NLTK | Text preprocessing |
| **Data Viz** | Chart.js | Interactive charts |
| **Storage** | Browser LocalStorage | Client-side persistence |

## 📦 Project Structure

```
SentiAnalyzer/
├── app.py                 # Main Flask application
├── train.py              # Model training script
├── preprocessing.py      # Text preprocessing utilities
├── evaluate.py           # Model evaluation script
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── model/
│   ├── model.pkl         # Trained classifier
│   └── vectorizer.pkl    # TF-IDF vectorizer
├── static/               # Static files (CSS, JS, images)
└── templates/            # HTML templates
```

## 🎓 Usage

### Web Interface

1. **Navigate to the Analyzer section**
2. **Enter your text** - Type or paste any text you want to analyze
3. **Click "Analyze Sentiment"** - Processing happens instantly
4. **View results**:
   - Sentiment classification (Positive/Negative)
   - Confidence percentage
   - Cleaned text after preprocessing
5. **Check statistics** - See aggregate analytics
6. **Review charts** - Visual representation of sentiment trends
7. **Browse history** - Last 50 analyses with timestamps

### API Usage

#### Health Check
```bash
curl http://localhost:5000/health
```

Response:
```json
{"status": "ok"}
```

#### Predict Sentiment
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "I love this amazing product!"}'
```

Response:
```json
{
  "sentiment": "Positive",
  "confidence": 0.95,
  "cleaned_text": "love amazing product"
}
```

## 📊 User Interface

### Sections

- **Navigation Bar** - Quick links to different sections
- **Header** - Professional branding and introduction
- **About** - Information about what the tool does and how it works
- **Analyzer** - Main text input and analysis form
- **Results** - Latest analysis with sentiment badge
- **Statistics** - Aggregate metrics (total, positive, negative, avg confidence)
- **Analytics** - Charts showing trends over time
- **History** - Log of all analyses with timestamps
- **Technology Stack** - Documentation of tools used

### Key Features

- **Sentiment Badges** - Color-coded indicators (green for positive, red for negative)
- **Confidence Display** - Visual percentage scores for reliability
- **History Tracking** - Persistent storage of analysis history
- **Real-time Charts** - Dynamic updates with each analysis
- **Responsive Design** - Mobile-friendly interface

## 🛠️ Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
FLASK_ENV=development
FLASK_DEBUG=False
```

### Customization

- **Port**: Edit `app.py` line for `app.run(port=5000)`
- **History Limit**: Modify `MAX_HISTORY = 50` in JavaScript
- **UI Theme**: Update CSS variables in `app.py`

## 📈 Model Performance

The sentiment classifier achieves:
- **Accuracy**: 85%+ on test data
- **Precision**: High confidence in predictions
- **Speed**: <100ms per prediction

*Performance metrics depend on training data quality and size*

## 🔐 Security

- No external API calls for data
- Client-side storage only
- No personal data collection
- Input validation and sanitization
- Error handling for edge cases

## 📝 Training Your Own Model

To train a custom model:

```bash
python train.py --data path/to/your/data.csv
```

Expected CSV format:
```
text,label
"Great product!",1
"Terrible experience",0
```

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit changes (`git commit -m 'Add YourFeature'`)
4. Push to branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## 🐛 Known Issues

- Browser LocalStorage has 5-10MB limit (typically handles 1000+ records)
- Long text (>10,000 characters) may take slightly longer to process
- Some special characters may be removed during preprocessing

## 🚀 Future Enhancements

- [ ] Multi-class sentiment analysis (Positive, Neutral, Negative)
- [ ] Aspect-based sentiment analysis
- [ ] Real-time social media monitoring
- [ ] Export analysis to CSV/PDF
- [ ] API authentication and rate limiting
- [ ] Database integration for scalability
- [ ] Docker containerization
- [ ] CI/CD pipeline

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**SentiAnalyzer Development Team**
- Year: 2026
- Version: 1.0
- Status: Production Ready ✅

## 📞 Support

For issues, questions, or suggestions:
- Open an [Issue](https://github.com/yourusername/SentiAnalyzer/issues)
- Start a [Discussion](https://github.com/yourusername/SentiAnalyzer/discussions)
- Email: your-email@example.com

## 🙏 Acknowledgments

Built with:
- [Flask](https://flask.palletsprojects.com/) - Web framework
- [scikit-learn](https://scikit-learn.org/) - Machine learning
- [NLTK](https://www.nltk.org/) - Natural language processing
- [Chart.js](https://www.chartjs.org/) - Data visualization

## 📊 Demo Data

Try these sample texts:

**Positive Examples:**
- "I absolutely love this product! It's amazing and works perfectly."
- "Great customer service and fast shipping!"
- "Best purchase I've made this year!"

**Negative Examples:**
- "Terrible quality and horrible customer support."
- "Complete waste of money, very disappointed."
- "Worst experience ever, would not recommend."

---

**Made with ❤️ for sentiment analysis enthusiasts**

Happy analyzing! 🎯
