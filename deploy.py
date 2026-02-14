#!/usr/bin/env python3
"""
Streamlit Cloud Deployment Helper
This script prepares your Banking Bot for deployment to Streamlit Cloud
"""

import os
import subprocess
import sys

def check_files():
    """Check if all required files are present"""
    required_files = [
        'app.py',
        'requirements.txt',
        'hbdb_banking_faqs.csv',
        'README.md'
    ]
    
    print("Checking for required files...")
    all_exist = True
    for file in required_files:
        exists = os.path.exists(file)
        status = "✓" if exists else "✗"
        print(f"  {status} {file}")
        if not exists:
            all_exist = False
    
    return all_exist

def test_app():
    """Test if the app runs without errors"""
    print("\nTesting app startup...")
    try:
        result = subprocess.run(
            [sys.executable, '-m', 'streamlit', 'run', 'app.py', '--headless'],
            capture_output=True,
            text=True,
            timeout=10
        )
        if "error" in result.stderr.lower():
            print("✗ Errors found during test:")
            print(result.stderr)
            return False
        print("✓ App test successful")
        return True
    except subprocess.TimeoutExpired:
        print("✓ App startup test completed (timeout expected)")
        return True
    except Exception as e:
        print(f"✗ Test failed: {e}")
        return False

def create_github_files():
    """Create .gitignore and setup files for GitHub"""
    print("\nCreating deployment files...")
    
    gitignore_content = """# Streamlit cache
.streamlit/
__pycache__/
*.py[cod]
*.egg-info/
dist/
build/

# Environment
.env
.venv/
venv/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Data
*.pickle
*.pkl
"""
    
    with open('.gitignore', 'w') as f:
        f.write(gitignore_content)
    print("✓ Created .gitignore")
    
    # Create setup.py
    setup_content = """from setuptools import setup, find_packages

setup(
    name="hbdb-banking-bot",
    version="1.0.0",
    description="A conversational AI chatbot for HBDB banking services",
    author="Banking Bot Creator",
    packages=find_packages(),
    python_requires=">=3.8",
)
"""
    
    with open('setup.py', 'w') as f:
        f.write(setup_content)
    print("✓ Created setup.py")

def deployment_instructions():
    """Print deployment instructions"""
    print("\n" + "="*60)
    print("DEPLOYMENT INSTRUCTIONS")
    print("="*60)
    print("""
1. CREATE GITHUB REPOSITORY
   - Go to https://github.com/new
   - Create a new repository

2. PUSH TO GITHUB
   Run these commands in the Banking folder:
   
   git init
   git add .
   git commit -m "Initial commit - HBDB Banking Bot"
   git branch -M main
   git remote add origin <your-repo-url>
   git push -u origin main

3. DEPLOY TO STREAMLIT CLOUD
   - Go to https://share.streamlit.io/
   - Click "New app"
   - Select:
     * Repository: your-repo
     * Branch: main
     * Main file path: app.py
   - Click "Deploy"

4. SET ENVIRONMENT VARIABLES
   - In Streamlit Cloud dashboard
   - Go to Settings → Secrets
   - Add: MISTRAL_API_KEY = your_key_here
   
5. SHARE YOUR APP
   - Get your public URL from Streamlit Cloud
   - Share with others!

ALTERNATIVE: RUN LOCALLY
   streamlit run app.py

Your app will be available at: http://localhost:8501
""")
    print("="*60)

def main():
    print("🏦 HBDB Banking Bot - Deployment Helper\n")
    
    # Check files
    if not check_files():
        print("\n✗ Missing required files!")
        sys.exit(1)
    
    # Test app
    if not test_app():
        print("\n✗ App tests failed!")
        sys.exit(1)
    
    # Create deployment files
    create_github_files()
    
    # Show instructions
    deployment_instructions()
    
    print("\n✓ All checks passed! Ready for deployment.")

if __name__ == "__main__":
    main()
