# Suspicious Domain Classifier

This project is a machine learning-based solution to detect potentially malicious or suspicious domains. It can be used in threat intelligence, phishing detection, and cybersecurity analytics.

## 🔧 Features
- Analyzes lexical patterns (length, digits, special chars, etc.)
- Checks domain WHOIS info and creation/expiry dates
- Uses public blacklists and threat intel sources
- Trains classifier models (RandomForest, SVM, etc.)
- Exports prediction results with confidence scores

## 🧠 Tech Stack
- Python
- Scikit-learn
- Pandas, NumPy
- WHOIS
- Public Blacklist APIs (optional)

## 🚀 How to Run

1. Install dependencies:
   
   pip install -r requirements.txt
   

2. Run the script:
   
   python main.py --input domains.txt
   

3. Output:
   - CSV file with predictions
   - Visualization (optional)

## 💡 Use Cases
- Cyber Threat Intelligence
- Anti-Phishing Engines
- Domain Risk Analysis

## 👤 Author  
Abhay Kumar Tripathi