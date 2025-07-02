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


## Screenshots
### Home Page
![image](https://github.com/user-attachments/assets/e4abd996-5ecd-4835-b69f-eb873e96cb8f)

### About Page
![image](https://github.com/user-attachments/assets/f555f6a5-0a03-4c35-92d8-5b5e303bf71d)

### Contact Page
![image](https://github.com/user-attachments/assets/7df00135-8a42-424f-9138-bae61a30e166)

### Predict
![image](https://github.com/user-attachments/assets/ff341b5b-34fe-4b71-aaac-1fec0653df04)
![image](https://github.com/user-attachments/assets/b750cb70-587e-461a-b305-753fd062c150)

### Result
![image](https://github.com/user-attachments/assets/49e8eec8-dd08-4471-9709-1ff059a7f04b)




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

