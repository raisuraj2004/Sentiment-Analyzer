#!/usr/bin/env python
"""
Script to push SentiAnalyzer to GitHub
Run this to automate the GitHub push process
"""

import os
import subprocess
import sys

def run_command(cmd, description):
    """Run a shell command and handle errors"""
    print(f"\n{'='*60}")
    print(f"📦 {description}...")
    print(f"{'='*60}")
    print(f"$ {cmd}\n")
    
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"\n❌ Error executing: {cmd}")
        return False
    return True

def main():
    os.chdir(r'C:\Users\raisu\OneDrive\Desktop\SentiAnalyzer')
    
    print("\n" + "="*60)
    print("🎯 SentiAnalyzer - GitHub Push Setup")
    print("="*60)
    
    # Step 1: Initialize git (if not already)
    if not os.path.exists('.git'):
        if not run_command('git init', 'Initializing Git repository'):
            return False
    else:
        print("\n✅ Git repository already initialized")
    
    # Step 2: Add remote
    print("\n" + "="*60)
    print("⚠️  MANUAL STEP REQUIRED")
    print("="*60)
    print("""
Please follow these steps to create GitHub repository and push:

1. CREATE REPOSITORY ON GITHUB:
   - Go to https://github.com/new
   - Repository name: SentiAnalyzer
   - Description: Professional Sentiment Analysis with ML
   - Choose Public or Private
   - Click "Create repository"

2. ADD REMOTE (copy the command from GitHub):
   git remote add origin https://github.com/YOUR_USERNAME/SentiAnalyzer.git
   
   (Replace YOUR_USERNAME with your GitHub username)

3. RUN THESE COMMANDS:
""")
    
    # Copy commands to clipboard
    commands = """
# Step 1: Replace old README
ren README.md README_OLD.md
ren README_NEW.md README.md

# Step 2: Rename old app.py backup
if exist app_old.py del app_old.py

# Step 3: Add all files to git
git add .

# Step 4: Create initial commit
git commit -m "Initial commit: SentiAnalyzer v1.0 - Professional Sentiment Analysis Platform

- Full-stack sentiment analysis application
- Flask REST API with modern web interface  
- Machine learning with scikit-learn and NLTK
- Real-time analytics and history tracking
- Responsive design with Chart.js visualizations
- Professional UI with gradient styling and animations"

# Step 5: Set main branch
git branch -M main

# Step 5: Push to GitHub (after adding remote)
git push -u origin main
"""
    
    print(commands)
    print("\n" + "="*60)
    print("📋 PASTE THE COMMANDS ABOVE IN YOUR TERMINAL")
    print("="*60 + "\n")

if __name__ == '__main__':
    main()
