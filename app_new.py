"""
SentiAnalyzer - Professional Sentiment Analysis Platform
Flask REST API and Web UI for sentiment analysis using machine learning
"""
import os
from flask import Flask, request, jsonify
import joblib
from preprocessing import clean_text
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Global variables for model and vectorizer
model = None
vectorizer = None


def load_model_and_vectorizer():
    """Load model and vectorizer at startup."""
    global model, vectorizer
    try:
        model = joblib.load('model/model.pkl')
        vectorizer = joblib.load('model/vectorizer.pkl')
        print("Model and vectorizer loaded successfully!")
    except FileNotFoundError:
        print(" Error: Model files not found. Please run train.py first.")
        raise


@app.route('/', methods=['GET'])
def home():
    """Root endpoint - serves the professional web UI."""
    html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SentiAnalyzer - Professional Sentiment Analysis</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><defs><linearGradient id='grad' x1='0%' y1='0%' x2='100%' y2='100%'><stop offset='0%' style='stop-color:%235a7cfa;stop-opacity:1' /><stop offset='100%' style='stop-color:%2374c0fc;stop-opacity:1' /></linearGradient></defs><rect width='100' height='100' fill='url(%23grad)' rx='20'/><circle cx='35' cy='40' r='15' fill='white'/><circle cx='65' cy='40' r='15' fill='white'/><path d='M 30 70 Q 50 85 70 70' stroke='white' stroke-width='6' fill='none' stroke-linecap='round'/></svg>">
    <style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

:root {
    --primary-color: #5a7cfa;
    --secondary-color: #74c0fc;
    --accent-color: #748ffc;
    --positive-color: #51cf66;
    --negative-color: #ff6b6b;
    --bg-light: #f5f7fa;
    --bg-white: #ffffff;
    --text-dark: #1a1a2e;
    --text-light: #6c757d;
    --border-color: #e9ecef;
    --shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
    --shadow-lg: 0 12px 24px rgba(0, 0, 0, 0.12);
    --shadow-xl: 0 20px 40px rgba(0, 0, 0, 0.15);
}

html { scroll-behavior: smooth; }

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif;
    background: linear-gradient(135deg, #f5f7fa 0%, #e9ecef 100%);
    color: var(--text-dark);
    line-height: 1.6;
}

.container {
    max-width: 1280px;
    margin: 0 auto;
    padding: 0 20px;
}

.navbar {
    background: var(--bg-white);
    box-shadow: var(--shadow);
    padding: 15px 0;
    position: sticky;
    top: 0;
    z-index: 100;
}

.navbar-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 1.3rem;
    font-weight: 700;
    background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.nav-links {
    display: flex;
    gap: 30px;
    list-style: none;
}

.nav-links a {
    text-decoration: none;
    color: var(--text-dark);
    font-weight: 500;
    transition: color 0.3s;
}

.nav-links a:hover { color: var(--primary-color); }

.header {
    background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 50%, var(--accent-color) 100%);
    color: white;
    padding: 80px 20px;
    text-align: center;
    margin-bottom: 50px;
    border-radius: 0 0 20px 20px;
    position: relative;
    overflow: hidden;
}

.header::before {
    content: '';
    position: absolute;
    top: -50%;
    right: -10%;
    width: 400px;
    height: 400px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 50%;
}

.header-content {
    position: relative;
    z-index: 1;
}

.header-content h1 {
    font-size: 3rem;
    margin-bottom: 15px;
    font-weight: 800;
    letter-spacing: -0.5px;
}

.header-content p {
    font-size: 1.2rem;
    opacity: 0.95;
    margin-bottom: 10px;
}

.header-subtitle {
    font-size: 0.95rem;
    opacity: 0.85;
}

.main-content { padding: 20px 0; }

.card {
    background: var(--bg-white);
    border-radius: 16px;
    padding: 35px;
    box-shadow: var(--shadow);
    margin-bottom: 30px;
    transition: all 0.3s ease;
    border: 1px solid rgba(255, 255, 255, 0.5);
}

.card:hover {
    box-shadow: var(--shadow-lg);
    transform: translateY(-2px);
}

.card h2 {
    color: var(--text-dark);
    margin-bottom: 25px;
    font-size: 1.6rem;
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 10px;
}

.about-section {
    background: linear-gradient(135deg, rgba(90, 124, 250, 0.05), rgba(116, 192, 252, 0.05));
    border: 2px solid rgba(90, 124, 250, 0.1);
    border-radius: 16px;
    padding: 40px;
    margin-bottom: 40px;
}

.about-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 30px;
    margin-top: 25px;
}

.about-card {
    background: white;
    padding: 25px;
    border-radius: 12px;
    box-shadow: var(--shadow);
}

.about-card h3 {
    color: var(--primary-color);
    margin-bottom: 15px;
    font-size: 1.2rem;
}

.about-card p {
    color: var(--text-light);
    line-height: 1.8;
}

.input-section { margin-bottom: 40px; }

.form-group { margin-bottom: 25px; }

.form-group label {
    display: block;
    margin-bottom: 10px;
    font-weight: 600;
    color: var(--text-dark);
}

.form-group textarea {
    width: 100%;
    padding: 15px;
    border: 2px solid var(--border-color);
    border-radius: 12px;
    font-size: 1rem;
    font-family: inherit;
    resize: vertical;
    transition: all 0.3s;
}

.form-group textarea:focus {
    outline: none;
    border-color: var(--primary-color);
    box-shadow: 0 0 0 4px rgba(90, 124, 250, 0.1);
}

.btn-analyze {
    background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    color: white;
    border: none;
    padding: 14px 40px;
    border-radius: 10px;
    font-size: 1.05rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s;
    box-shadow: var(--shadow);
}

.btn-analyze:hover {
    transform: translateY(-3px);
    box-shadow: var(--shadow-lg);
}

.btn-analyze:active { transform: translateY(-1px); }

.loading {
    text-align: center;
    padding: 30px;
}

.spinner {
    border: 4px solid var(--border-color);
    border-top: 4px solid var(--primary-color);
    border-radius: 50%;
    width: 50px;
    height: 50px;
    animation: spin 1s linear infinite;
    margin: 0 auto 15px;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

.results-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 25px;
    margin-bottom: 40px;
}

.result-content { animation: slideIn 0.4s ease; }

@keyframes slideIn {
    from { opacity: 0; transform: translateY(15px); }
    to { opacity: 1; transform: translateY(0); }
}

.sentiment-badge {
    padding: 25px;
    border-radius: 12px;
    text-align: center;
    margin-bottom: 20px;
    font-size: 1.4rem;
    font-weight: 700;
}

.sentiment-badge.positive {
    background: linear-gradient(135deg, #d3f9d8, #c3e7cb);
    color: #2b8a3e;
    border: 2px solid var(--positive-color);
    box-shadow: 0 10px 25px rgba(81, 207, 102, 0.2);
}

.sentiment-badge.negative {
    background: linear-gradient(135deg, #ffe0e0, #ffc9c9);
    color: #c92a2a;
    border: 2px solid var(--negative-color);
    box-shadow: 0 10px 25px rgba(255, 107, 107, 0.2);
}

.cleaned-text {
    background-color: var(--bg-light);
    padding: 15px;
    border-radius: 10px;
    border-left: 4px solid var(--primary-color);
    font-style: italic;
    color: var(--text-light);
    line-height: 1.7;
}

.no-result {
    text-align: center;
    color: var(--text-light);
    padding: 30px;
}

.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 15px;
}

.stat-box {
    background: linear-gradient(135deg, #f8f9fa, #e9ecef);
    padding: 25px;
    border-radius: 12px;
    text-align: center;
    transition: all 0.3s;
    border: 1px solid rgba(90, 124, 250, 0.1);
}

.stat-box:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-lg);
}

.stat-box h3 {
    font-size: 2rem;
    color: var(--primary-color);
    margin-bottom: 8px;
}

.stat-box p {
    color: var(--text-light);
    font-size: 0.9rem;
    font-weight: 500;
}

.charts-section { margin-bottom: 40px; }

.chart-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 25px;
}

.chart-container {
    background: var(--bg-white);
    padding: 25px;
    border-radius: 12px;
    box-shadow: var(--shadow);
}

.chart-container h3 {
    margin-bottom: 20px;
    color: var(--text-dark);
    font-weight: 600;
}

.history-content {
    max-height: 450px;
    overflow-y: auto;
}

.history-item {
    background: var(--bg-light);
    padding: 18px;
    border-radius: 10px;
    margin-bottom: 12px;
    border-left: 4px solid var(--primary-color);
    transition: all 0.2s;
}

.history-item:hover { box-shadow: var(--shadow); }

.history-item-text {
    font-size: 0.95rem;
    color: var(--text-dark);
    margin-bottom: 10px;
    word-break: break-word;
}

.history-item-meta {
    display: flex;
    justify-content: space-between;
    font-size: 0.85rem;
}

.history-sentiment {
    font-weight: 600;
    padding: 4px 10px;
    border-radius: 6px;
}

.history-sentiment.positive {
    background-color: #d3f9d8;
    color: #2b8a3e;
}

.history-sentiment.negative {
    background-color: #ffe0e0;
    color: #c92a2a;
}

.no-history {
    text-align: center;
    color: var(--text-light);
    padding: 30px;
}

.footer {
    background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    color: white;
    text-align: center;
    padding: 40px 20px;
    margin-top: 80px;
    border-radius: 20px 20px 0 0;
}

.footer h3 { margin-bottom: 10px; }

.tech-stack {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-top: 15px;
    flex-wrap: wrap;
    font-size: 0.9rem;
}

@media (max-width: 768px) {
    .header-content h1 { font-size: 2rem; }
    .results-container { grid-template-columns: 1fr; }
    .chart-grid { grid-template-columns: 1fr; }
    .stats-grid { grid-template-columns: repeat(2, 1fr); }
    .nav-links { gap: 15px; font-size: 0.9rem; }
    .card { padding: 20px; }
}

::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: var(--bg-light); }
::-webkit-scrollbar-thumb { background: var(--primary-color); border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: var(--accent-color); }
    </style>
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <div class="navbar-content">
                <div class="logo">
                    <span></span> SentiAnalyzer
                </div>
                <ul class="nav-links">
                    <li><a href="#analyze">Analyze</a></li>
                    <li><a href="#about">About</a></li>
                    <li><a href="#tech">Technology</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <header class="header">
        <div class="header-content">
            <h1> SentiAnalyzer</h1>
            <p>Professional Sentiment Analysis Platform</p>
            <p class="header-subtitle">Analyze text emotions with advanced machine learning</p>
        </div>
    </header>

    <div class="container">
        <main class="main-content">
            <section class="about-section" id="about">
                <h2> About SentiAnalyzer</h2>
                <div class="about-grid">
                    <div class="about-card">
                        <h3> What It Does</h3>
                        <p>SentiAnalyzer uses advanced machine learning to analyze the emotional sentiment of any text. It classifies content as <strong>Positive</strong> or <strong>Negative</strong> and provides confidence scores to measure prediction reliability.</p>
                    </div>
                    <div class="about-card">
                        <h3> How It Works</h3>
                        <p>The system uses text preprocessing, feature extraction via TF-IDF vectorization, and trained classification algorithms. Text is cleaned, normalized, and converted to numerical features for model prediction.</p>
                    </div>
                    <div class="about-card">
                        <h3> Use Cases</h3>
                        <p>Perfect for analyzing customer reviews, social media comments, feedback surveys, product ratings, brand sentiment monitoring, and real-time opinion mining from any text source.</p>
                    </div>
                </div>
            </section>

            <section class="input-section" id="analyze">
                <div class="card">
                    <h2> Analyze Your Text</h2>
                    <form id="sentimentForm">
                        <div class="form-group">
                            <label for="textInput">Enter Text for Analysis:</label>
                            <textarea 
                                id="textInput" 
                                placeholder="Type or paste your text here. Examples: 'I love this product!' or 'This was a terrible experience.'" 
                                rows="4"
                                required
                            ></textarea>
                        </div>
                        <button type="submit" class="btn-analyze">🔍 Analyze Sentiment</button>
                    </form>
                    <div id="loading" class="loading" style="display:none;">
                        <div class="spinner"></div>
                        <p>Analyzing your text...</p>
                    </div>
                </div>
            </section>

            <div class="results-container">
                <section>
                    <div class="card">
                        <h2> Analysis Result</h2>
                        <div id="resultContent" class="result-content" style="display:none;">
                            <div class="sentiment-badge" id="sentimentBadge"></div>
                            <div class="result-details">
                                <p><strong>Confidence Score:</strong> <span id="confidenceScore">-</span>%</p>
                                <p><strong>Processed Text:</strong></p>
                                <div class="cleaned-text" id="cleanedText"></div>
                            </div>
                        </div>
                        <div id="noResult" class="no-result">No analysis yet. Enter text above to begin.</div>
                    </div>
                </section>

                <section>
                    <div class="card">
                        <h2>Statistics</h2>
                        <div class="stats-grid">
                            <div class="stat-box">
                                <h3 id="totalAnalyses">0</h3>
                                <p>Total Analyses</p>
                            </div>
                            <div class="stat-box">
                                <h3 id="positiveCount">0</h3>
                                <p>Positive</p>
                            </div>
                            <div class="stat-box">
                                <h3 id="negativeCount">0</h3>
                                <p>Negative</p>
                            </div>
                            <div class="stat-box">
                                <h3 id="avgConfidence">0%</h3>
                                <p>Avg Confidence</p>
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <section class="charts-section">
                <div class="card">
                    <h2> Analytics & Insights</h2>
                    <div class="chart-grid">
                        <div class="chart-container">
                            <h3>Sentiment Distribution</h3>
                            <canvas id="sentimentChart"></canvas>
                        </div>
                        <div class="chart-container">
                            <h3>Confidence Over Time</h3>
                            <canvas id="confidenceChart"></canvas>
                        </div>
                    </div>
                </div>
            </section>

            <section>
                <div class="card">
                    <h2> Analysis History</h2>
                    <div id="historyContent" class="history-content">
                        <p class="no-history">No analysis history yet.</p>
                    </div>
                </div>
            </section>

            <section class="about-section" id="tech" style="margin-top: 50px;">
                <h2> Technology Stack</h2>
                <div class="about-grid" style="margin-top: 25px;">
                    <div class="about-card">
                        <h3>Backend</h3>
                        <p><strong>Flask</strong> - Python REST API framework for handling requests and predictions</p>
                    </div>
                    <div class="about-card">
                        <h3>Machine Learning</h3>
                        <p><strong>scikit-learn</strong> - For model training, vectorization (TF-IDF), and classification</p>
                    </div>
                    <div class="about-card">
                        <h3>Frontend</h3>
                        <p><strong>HTML5, CSS3, Vanilla JS</strong> - Modern, responsive web interface</p>
                    </div>
                    <div class="about-card">
                        <h3>Data Visualization</h3>
                        <p><strong>Chart.js</strong> - Interactive charts for sentiment trends and analytics</p>
                    </div>
                    <div class="about-card">
                        <h3>Data Storage</h3>
                        <p><strong>LocalStorage</strong> - Client-side persistence for analysis history</p>
                    </div>
                    <div class="about-card">
                        <h3>NLP Processing</h3>
                        <p><strong>NLTK</strong> - Text preprocessing, tokenization, and cleaning</p>
                    </div>
                </div>
            </section>

        </main>
    </div>

    <footer class="footer">
        <h3> SentiAnalyzer v1.0</h3>
        <p>Advanced Sentiment Analysis with Machine Learning</p>
        <div class="tech-stack">
            <span> Python</span>
            <span> Flask</span>
            <span> scikit-learn</span>
            <span> Chart.js</span>
            <span> Modern UI/UX</span>
        </div>
        <p style="margin-top: 20px; opacity: 0.9;">&copy; 2026 SentiAnalyzer. All rights reserved.</p>
    </footer>

    <script>
let analysisHistory = [];
let sentimentChart = null;
let confidenceChart = null;

document.addEventListener('DOMContentLoaded', function() {
    loadHistoryFromStorage();
    initializeCharts();
    document.getElementById('sentimentForm').addEventListener('submit', handleFormSubmit);
});

async function handleFormSubmit(e) {
    e.preventDefault();
    const text = document.getElementById('textInput').value.trim();
    if (!text) {
        alert('Please enter some text to analyze');
        return;
    }

    document.getElementById('loading').style.display = 'block';

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text: text })
        });

        if (!response.ok) throw new Error('Failed to analyze');

        const data = await response.json();
        displayResult(data);
        addToHistory(data);
        updateStatistics();
        updateCharts();
        document.getElementById('textInput').value = '';
    } catch (error) {
        alert('Error: ' + error.message);
    } finally {
        document.getElementById('loading').style.display = 'none';
    }
}

function displayResult(data) {
    const sentiment = data.sentiment;
    const confidence = Math.round(data.confidence * 100);
    const badge = document.getElementById('sentimentBadge');
    
    badge.className = 'sentiment-badge ' + sentiment.toLowerCase();
    badge.innerHTML = `<strong>${sentiment}</strong><br><small>${confidence}% confident</small>`;
    
    document.getElementById('confidenceScore').textContent = confidence;
    document.getElementById('cleanedText').textContent = data.cleaned_text;
    document.getElementById('resultContent').style.display = 'block';
    document.getElementById('noResult').style.display = 'none';
}

function addToHistory(data) {
    const timestamp = new Date().toLocaleTimeString();
    analysisHistory.unshift({
        text: data.cleaned_text,
        sentiment: data.sentiment,
        confidence: data.confidence,
        timestamp: timestamp
    });
    
    if (analysisHistory.length > 50) analysisHistory.pop();
    saveHistoryToStorage();
    updateHistoryDisplay();
}

function updateHistoryDisplay() {
    const container = document.getElementById('historyContent');
    if (analysisHistory.length === 0) {
        container.innerHTML = '<p class="no-history">No analysis history yet.</p>';
        return;
    }

    container.innerHTML = analysisHistory.map(item => `
        <div class="history-item">
            <div class="history-item-text">"${item.text.substring(0, 100)}${item.text.length > 100 ? '...' : ''}"</div>
            <div class="history-item-meta">
                <span class="history-sentiment ${item.sentiment.toLowerCase()}">
                    ${item.sentiment} (${Math.round(item.confidence * 100)}%)
                </span>
                <span>${item.timestamp}</span>
            </div>
        </div>
    `).join('');
}

function updateStatistics() {
    const total = analysisHistory.length;
    const positive = analysisHistory.filter(i => i.sentiment === 'Positive').length;
    const negative = analysisHistory.filter(i => i.sentiment === 'Negative').length;
    const avg = total > 0 ? Math.round(analysisHistory.reduce((s, i) => s + i.confidence, 0) / total * 100) : 0;

    document.getElementById('totalAnalyses').textContent = total;
    document.getElementById('positiveCount').textContent = positive;
    document.getElementById('negativeCount').textContent = negative;
    document.getElementById('avgConfidence').textContent = avg + '%';
}

function initializeCharts() {
    sentimentChart = new Chart(document.getElementById('sentimentChart'), {
        type: 'doughnut',
        data: {
            labels: ['Positive', 'Negative'],
            datasets: [{
                data: [0, 0],
                backgroundColor: ['#51cf66', '#ff6b6b'],
                borderColor: ['#ffffff', '#ffffff'],
                borderWidth: 2
            }]
        },
        options: { responsive: true, plugins: { legend: { position: 'bottom' } } }
    });

    confidenceChart = new Chart(document.getElementById('confidenceChart'), {
        type: 'line',
        data: { labels: [], datasets: [{ label: 'Confidence Score', data: [], borderColor: '#5a7cfa', backgroundColor: 'rgba(90, 124, 250, 0.1)', borderWidth: 2, fill: true, tension: 0.4, pointRadius: 5 }] },
        options: { responsive: true, scales: { y: { beginAtZero: true, max: 1, ticks: { callback: v => Math.round(v * 100) + '%' } } } }
    });
}

function updateCharts() {
    if (analysisHistory.length === 0) return;
    const pos = analysisHistory.filter(i => i.sentiment === 'Positive').length;
    sentimentChart.data.datasets[0].data = [pos, analysisHistory.length - pos];
    sentimentChart.update();

    const recent = analysisHistory.slice(0, 10).reverse();
    confidenceChart.data.labels = recent.map((_, i) => `#${i + 1}`);
    confidenceChart.data.datasets[0].data = recent.map(i => i.confidence);
    confidenceChart.update();
}

function saveHistoryToStorage() {
    localStorage.setItem('sentimentHistory', JSON.stringify(analysisHistory));
}

function loadHistoryFromStorage() {
    const stored = localStorage.getItem('sentimentHistory');
    if (stored) {
        analysisHistory = JSON.parse(stored);
        updateHistoryDisplay();
        updateStatistics();
        updateCharts();
    }
}
    </script>
</body>
</html>'''
    return html


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({"status": "ok"}), 200


@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict sentiment of input text.
    
    Expected JSON: {"text": "your text here"}
    Returns: {"sentiment": "Positive" or "Negative", "confidence": float, "cleaned_text": str}
    """
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({"error": "Missing 'text' field in request"}), 400
        
        text = data['text']
        
        if not text or not isinstance(text, str):
            return jsonify({"error": "Text must be a non-empty string"}), 400
        
        cleaned_text = clean_text(text)
        
        if not cleaned_text:
            return jsonify({"error": "Text becomes empty after cleaning"}), 400
        
        text_vec = vectorizer.transform([cleaned_text])
        prediction = model.predict(text_vec)[0]
        confidence = max(model.predict_proba(text_vec)[0])
        sentiment = "Positive" if prediction == 1 else "Negative"
        
        return jsonify({
            "sentiment": sentiment,
            "confidence": round(float(confidence), 2),
            "cleaned_text": cleaned_text
        }), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(405)
def method_not_allowed(error):
    """Handle 405 errors."""
    return jsonify({"error": "Method not allowed"}), 405


if __name__ == '__main__':
    load_model_and_vectorizer()
    print("\n" + "="*60)
    print(" SentiAnalyzer - Professional Sentiment Analysis")
    print("="*60)
    print(" Open your browser to: http://localhost:5000")
    print(" API endpoints available at /health and /predict")
    print("="*60 + "\n")
    app.run(host='0.0.0.0', port=5000, debug=False)
