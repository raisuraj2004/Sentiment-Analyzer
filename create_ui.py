#!/usr/bin/env python
"""Script to create UI files for SentiAnalyzer"""
import os

# Create directories
os.makedirs('templates', exist_ok=True)
os.makedirs('static', exist_ok=True)

# HTML Template
html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SentiAnalyzer - Sentiment Analysis</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <div class="container">
        <!-- Header -->
        <header class="header">
            <div class="header-content">
                <h1> SentiAnalyzer</h1>
                <p>Advanced Sentiment Analysis Tool</p>
            </div>
        </header>

        <main class="main-content">
            <!-- Input Section -->
            <section class="input-section">
                <div class="card">
                    <h2>Analyze Your Text</h2>
                    <form id="sentimentForm">
                        <div class="form-group">
                            <label for="textInput">Enter Text:</label>
                            <textarea 
                                id="textInput" 
                                placeholder="Type or paste your text here..." 
                                rows="4"
                                required
                            ></textarea>
                        </div>
                        <button type="submit" class="btn-analyze">Analyze Sentiment</button>
                    </form>
                    <div id="loading" class="loading" style="display:none;">
                        <div class="spinner"></div>
                        <p>Analyzing...</p>
                    </div>
                </div>
            </section>

            <!-- Results Section -->
            <div class="results-container">
                <section class="result-section">
                    <div class="card">
                        <h2>Latest Analysis</h2>
                        <div id="resultContent" class="result-content" style="display:none;">
                            <div class="sentiment-badge" id="sentimentBadge"></div>
                            <div class="result-details">
                                <p><strong>Confidence:</strong> <span id="confidenceScore">-</span>%</p>
                                <p><strong>Cleaned Text:</strong></p>
                                <div class="cleaned-text" id="cleanedText"></div>
                            </div>
                        </div>
                        <div id="noResult" class="no-result">No analysis yet. Start by entering text above.</div>
                    </div>
                </section>

                <!-- Statistics Section -->
                <section class="stats-section">
                    <div class="card">
                        <h2>Analysis Statistics</h2>
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

            <!-- Charts Section -->
            <section class="charts-section">
                <div class="card">
                    <h2>Analytics</h2>
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

            <!-- History Section -->
            <section class="history-section">
                <div class="card">
                    <h2>Analysis History</h2>
                    <div id="historyContent" class="history-content">
                        <p class="no-history">No analysis history yet.</p>
                    </div>
                </div>
            </section>
        </main>

        <!-- Footer -->
        <footer class="footer">
            <p>&copy; 2026 SentiAnalyzer. All rights reserved.</p>
        </footer>
    </div>

    <script src="{{ url_for('static', filename='script.js') }}"></script>
</body>
</html>
'''

# CSS Stylesheet
css_content = '''* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

:root {
    --primary-color: #5a7cfa;
    --secondary-color: #74c0fc;
    --positive-color: #51cf66;
    --negative-color: #ff6b6b;
    --bg-light: #f8f9fa;
    --bg-white: #ffffff;
    --text-dark: #212529;
    --text-light: #6c757d;
    --border-color: #e9ecef;
    --shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    --shadow-lg: 0 8px 16px rgba(0, 0, 0, 0.12);
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    background-color: #f5f7fa;
    color: var(--text-dark);
    line-height: 1.6;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

/* Header */
.header {
    background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    color: white;
    padding: 60px 20px;
    text-align: center;
    margin-bottom: 40px;
    box-shadow: var(--shadow-lg);
}

.header-content h1 {
    font-size: 2.5rem;
    margin-bottom: 10px;
    font-weight: 700;
}

.header-content p {
    font-size: 1.1rem;
    opacity: 0.95;
}

/* Main Content */
.main-content {
    padding: 20px 0;
}

/* Cards */
.card {
    background: var(--bg-white);
    border-radius: 12px;
    padding: 30px;
    box-shadow: var(--shadow);
    margin-bottom: 25px;
    transition: box-shadow 0.3s ease;
}

.card:hover {
    box-shadow: var(--shadow-lg);
}

.card h2 {
    color: var(--text-dark);
    margin-bottom: 20px;
    font-size: 1.5rem;
    font-weight: 600;
}

.card h3 {
    color: var(--text-dark);
    margin-bottom: 15px;
    font-size: 1.1rem;
}

/* Input Section */
.input-section {
    margin-bottom: 40px;
}

.form-group {
    margin-bottom: 20px;
}

.form-group label {
    display: block;
    margin-bottom: 8px;
    font-weight: 500;
    color: var(--text-dark);
}

.form-group textarea {
    width: 100%;
    padding: 12px;
    border: 2px solid var(--border-color);
    border-radius: 8px;
    font-size: 1rem;
    font-family: inherit;
    resize: vertical;
    transition: border-color 0.3s ease;
}

.form-group textarea:focus {
    outline: none;
    border-color: var(--primary-color);
    box-shadow: 0 0 0 3px rgba(90, 124, 250, 0.1);
}

/* Buttons */
.btn-analyze {
    background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    color: white;
    border: none;
    padding: 12px 32px;
    border-radius: 8px;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.btn-analyze:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-lg);
}

.btn-analyze:active {
    transform: translateY(0);
}

/* Loading */
.loading {
    text-align: center;
    padding: 20px;
}

.spinner {
    border: 4px solid var(--border-color);
    border-top: 4px solid var(--primary-color);
    border-radius: 50%;
    width: 40px;
    height: 40px;
    animation: spin 1s linear infinite;
    margin: 0 auto 10px;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

/* Results Container */
.results-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 25px;
    margin-bottom: 40px;
}

.result-content {
    animation: slideIn 0.3s ease;
}

@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateY(10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Sentiment Badge */
.sentiment-badge {
    padding: 20px;
    border-radius: 8px;
    text-align: center;
    margin-bottom: 20px;
    font-size: 1.3rem;
    font-weight: 600;
}

.sentiment-badge.positive {
    background-color: #d3f9d8;
    color: #2b8a3e;
    border: 2px solid var(--positive-color);
}

.sentiment-badge.negative {
    background-color: #ffe0e0;
    color: #c92a2a;
    border: 2px solid var(--negative-color);
}

.result-details {
    color: var(--text-dark);
}

.result-details p {
    margin-bottom: 12px;
}

.cleaned-text {
    background-color: var(--bg-light);
    padding: 12px;
    border-radius: 6px;
    border-left: 4px solid var(--primary-color);
    font-style: italic;
    color: var(--text-light);
}

.no-result {
    text-align: center;
    color: var(--text-light);
    padding: 20px;
}

/* Stats Grid */
.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 15px;
}

.stat-box {
    background: linear-gradient(135deg, #f8f9fa, #e9ecef);
    padding: 20px;
    border-radius: 8px;
    text-align: center;
    transition: transform 0.3s ease;
}

.stat-box:hover {
    transform: translateY(-5px);
}

.stat-box h3 {
    font-size: 1.8rem;
    color: var(--primary-color);
    margin-bottom: 5px;
}

.stat-box p {
    color: var(--text-light);
    font-size: 0.9rem;
}

/* Charts Section */
.charts-section {
    margin-bottom: 40px;
}

.chart-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 25px;
}

.chart-container {
    background: var(--bg-light);
    padding: 20px;
    border-radius: 8px;
}

.chart-container h3 {
    margin-bottom: 15px;
    color: var(--text-dark);
}

/* History Section */
.history-content {
    max-height: 400px;
    overflow-y: auto;
}

.history-item {
    background: var(--bg-light);
    padding: 15px;
    border-radius: 6px;
    margin-bottom: 10px;
    border-left: 4px solid var(--primary-color);
}

.history-item-text {
    font-size: 0.95rem;
    color: var(--text-dark);
    margin-bottom: 8px;
    word-break: break-word;
}

.history-item-meta {
    display: flex;
    justify-content: space-between;
    font-size: 0.85rem;
    color: var(--text-light);
}

.history-sentiment {
    font-weight: 600;
    padding: 2px 8px;
    border-radius: 4px;
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
    padding: 20px;
}

/* Footer */
.footer {
    background-color: var(--bg-light);
    text-align: center;
    padding: 30px 20px;
    color: var(--text-light);
    margin-top: 60px;
    border-top: 1px solid var(--border-color);
}

/* Responsive */
@media (max-width: 768px) {
    .header-content h1 {
        font-size: 1.8rem;
    }

    .results-container {
        grid-template-columns: 1fr;
    }

    .chart-grid {
        grid-template-columns: 1fr;
    }

    .stats-grid {
        grid-template-columns: repeat(2, 1fr);
    }

    .card {
        padding: 20px;
    }
}
'''

# JavaScript
js_content = '''// State management
let analysisHistory = [];
let sentimentChart = null;
let confidenceChart = null;

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    loadHistoryFromStorage();
    initializeCharts();
    setupEventListeners();
});

function setupEventListeners() {
    document.getElementById('sentimentForm').addEventListener('submit', handleFormSubmit);
}

async function handleFormSubmit(e) {
    e.preventDefault();
    
    const text = document.getElementById('textInput').value.trim();
    if (!text) {
        alert('Please enter some text to analyze');
        return;
    }

    showLoading(true);

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: text })
        });

        if (!response.ok) {
            throw new Error('Failed to analyze sentiment');
        }

        const data = await response.json();
        displayResult(data);
        addToHistory(data);
        updateStatistics();
        updateCharts();
        
        document.getElementById('textInput').value = '';
    } catch (error) {
        alert('Error: ' + error.message);
    } finally {
        showLoading(false);
    }
}

function showLoading(show) {
    document.getElementById('loading').style.display = show ? 'block' : 'none';
}

function displayResult(data) {
    const resultContent = document.getElementById('resultContent');
    const noResult = document.getElementById('noResult');
    const badge = document.getElementById('sentimentBadge');
    
    const sentiment = data.sentiment;
    const confidence = Math.round(data.confidence * 100);
    const cleanedText = data.cleaned_text;

    badge.className = 'sentiment-badge ' + sentiment.toLowerCase();
    badge.innerHTML = `<strong>${sentiment}</strong><br><small>${confidence}% confident</small>`;
    
    document.getElementById('confidenceScore').textContent = confidence;
    document.getElementById('cleanedText').textContent = cleanedText;

    resultContent.style.display = 'block';
    noResult.style.display = 'none';
}

function addToHistory(data) {
    const timestamp = new Date().toLocaleTimeString();
    const historyItem = {
        text: data.cleaned_text,
        sentiment: data.sentiment,
        confidence: data.confidence,
        timestamp: timestamp
    };
    
    analysisHistory.unshift(historyItem);
    if (analysisHistory.length > 50) {
        analysisHistory.pop();
    }
    
    saveHistoryToStorage();
    updateHistoryDisplay();
}

function updateHistoryDisplay() {
    const historyContent = document.getElementById('historyContent');
    
    if (analysisHistory.length === 0) {
        historyContent.innerHTML = '<p class="no-history">No analysis history yet.</p>';
        return;
    }

    historyContent.innerHTML = analysisHistory.map((item, index) => `
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
    const positive = analysisHistory.filter(item => item.sentiment === 'Positive').length;
    const negative = analysisHistory.filter(item => item.sentiment === 'Negative').length;
    const avgConfidence = total > 0 
        ? Math.round((analysisHistory.reduce((sum, item) => sum + item.confidence, 0) / total) * 100)
        : 0;

    document.getElementById('totalAnalyses').textContent = total;
    document.getElementById('positiveCount').textContent = positive;
    document.getElementById('negativeCount').textContent = negative;
    document.getElementById('avgConfidence').textContent = avgConfidence + '%';
}

function initializeCharts() {
    const sentimentCtx = document.getElementById('sentimentChart').getContext('2d');
    sentimentChart = new Chart(sentimentCtx, {
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
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    position: 'bottom'
                }
            }
        }
    });

    const confidenceCtx = document.getElementById('confidenceChart').getContext('2d');
    confidenceChart = new Chart(confidenceCtx, {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: 'Confidence Score',
                data: [],
                borderColor: '#5a7cfa',
                backgroundColor: 'rgba(90, 124, 250, 0.1)',
                borderWidth: 2,
                fill: true,
                tension: 0.4,
                pointBackgroundColor: '#5a7cfa',
                pointBorderColor: '#ffffff',
                pointBorderWidth: 2,
                pointRadius: 5
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            scales: {
                y: {
                    beginAtZero: true,
                    max: 1,
                    ticks: {
                        callback: function(value) {
                            return Math.round(value * 100) + '%';
                        }
                    }
                }
            },
            plugins: {
                legend: {
                    display: true,
                    position: 'top'
                }
            }
        }
    });
}

function updateCharts() {
    if (analysisHistory.length === 0) return;

    // Update sentiment distribution
    const positive = analysisHistory.filter(item => item.sentiment === 'Positive').length;
    const negative = analysisHistory.filter(item => item.sentiment === 'Negative').length;
    
    sentimentChart.data.datasets[0].data = [positive, negative];
    sentimentChart.update();

    // Update confidence over time (last 10)
    const recentHistory = analysisHistory.slice(0, 10).reverse();
    confidenceChart.data.labels = recentHistory.map((_, i) => `#${i + 1}`);
    confidenceChart.data.datasets[0].data = recentHistory.map(item => item.confidence);
    confidenceChart.update();
}

// LocalStorage functions
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
'''

# Write files
with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
print('✓ Created templates/index.html')

with open('static/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)
print('✓ Created static/style.css')

with open('static/script.js', 'w', encoding='utf-8') as f:
    f.write(js_content)
print('✓ Created static/script.js')

print('\n All UI files created successfully!')
