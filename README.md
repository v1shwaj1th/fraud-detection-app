# 🛡️ Insurance Fraud Detection System

A full-stack machine learning web application to detect fraudulent insurance claims using a Random Forest classifier. The project integrates a user-friendly UI, real-time prediction, and reliable deployment—all aimed at reducing insurance fraud and protecting stakeholders.

## 🚀 Live Demo

👉 [View Live App] https://insurance-fraud-detector-bvjh.onrender.com/

## 🧠 Machine Learning Pipeline

- **Models Evaluated**: Logistic Regression, Decision Tree, Random Forest, XGBoost  
- **Selected Model**: Random Forest (92% accuracy, high F1-score)  
- **Preprocessing**:  
  - Label Encoding for categorical features  
  - Feature selection using Recursive Feature Elimination (RFE)  
  - Standard Scaling  
  - SMOTE for class imbalance handling  

## 🌐 Features

- 🔍 Real-time fraud prediction with clear result feedback  
- 🧾 Dynamic input form with label encoding and options based on training data  
- 🔄 Session-based result display with conditional styling  
- 📄 Informational pages: About, Contact (IRDAI), and How to Report Fraud  
- 🚀 Deployed on **Render**, with average API response time under **400ms**

## 🛠️ Tech Stack

| Category         | Tools Used                           |
|------------------|--------------------------------------|
| Frontend         | HTML, Tailwind CSS, Jinja2           |
| Backend          | Python, Flask                        |
| ML & Data        | Scikit-learn, Pandas, NumPy, SMOTE   |
| Deployment       | Render                               |
| Others           | Jupyter Notebook, Pickle             |

## 📁 Project Structure

```
📦 project/
├── static/
│   └── images/...
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── about.html
│   ├── contact.html
│   ├── predict.html
│   └── result.html
├── fraud_rf_model.pkl
├── scaler.pkl
├── label_encoders.pkl
├── selected_features.pkl
├── input_options.pkl
├── app.py
└── README.md
```

## ⚙️ Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
git clone https://github.com/your-username/insurance-fraud-detection.git
cd insurance-fraud-detection
pip install -r requirements.txt
```

### Run Locally

```bash
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

## 👥 Team

- **Team Lead**: K Vishwajith 
- **Contributors**: Ayaan Gupta, Advesh Darvekar

