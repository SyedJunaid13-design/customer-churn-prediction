# 📊 Customer Churn Prediction

An end-to-end Machine Learning project that predicts whether a telecom customer is likely to churn based on their demographic, service, contract, and billing information.

The project includes data analysis, visualization, model comparison, hyperparameter tuning, and an interactive Streamlit web application.

---

## 🎯 Project Objective

Customer churn is an important business problem for subscription-based companies.

The objective of this project is to:

- Analyze customer behavior
- Identify patterns associated with churn
- Build machine learning classification models
- Compare model performance
- Select and tune a suitable final model
- Provide an easy-to-use interface for predicting customer churn risk

---

## 🧠 Machine Learning Workflow

The project follows a complete machine learning workflow:

```text
Dataset
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Data Preprocessing
   ↓
Train / Test Split
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Model Comparison
   ↓
Hyperparameter Tuning
   ↓
Final Model
   ↓
Streamlit Web Application

📊 Dataset

This project uses the Telco Customer Churn dataset.

The dataset contains information about:

Customer demographics
Customer tenure
Phone services
Internet services
Online security and backup
Technical support
Streaming services
Contract information
Payment methods
Monthly charges
Total charges
Customer churn status
Target Variable

Churn

Yes → Customer left the company
No → Customer stayed with the company
🔍 Exploratory Data Analysis

Exploratory Data Analysis was performed to understand customer behavior and identify patterns related to churn.

The analysis examined relationships between churn and factors such as:

Contract type
Customer tenure
Monthly charges
Internet service
Payment method
Technical support
Online security
Customer services
Customer demographics

Visualizations were used to identify important patterns and understand which customer characteristics may be associated with higher churn risk.

🤖 Machine Learning Models

Three classification algorithms were evaluated:

1. Logistic Regression

Logistic Regression was used as the final prediction model because it provided strong ROC-AUC performance and is relatively easy to interpret for a business classification problem.

2. Decision Tree

Decision Tree was used to capture nonlinear relationships between customer characteristics and churn.

3. Random Forest

Random Forest was evaluated as an ensemble learning approach using multiple decision trees.

📈 Model Performance
Model	Accuracy	ROC-AUC
Logistic Regression	80.55%	84.21%
Decision Tree	79.84%	82.97%
Random Forest	80.77%	84.22%

The models achieved similar overall performance.

Logistic Regression was selected as the final model because it provided strong performance while remaining relatively interpretable for a business use case.

⚙️ Hyperparameter Tuning

Grid Search with 5-fold cross-validation was used to optimize the Logistic Regression model.

Best Parameter
C = 10
Best Cross-Validation ROC-AUC
0.8459

The tuned model was then evaluated on the test dataset.

🖥️ Interactive Web Application

A Streamlit web application was developed to make the machine learning model accessible to non-technical users.

Users can enter:

👤 Customer Information
Gender
Senior citizen status
Partner status
Dependents
Customer tenure
📡 Services
Phone service
Multiple phone lines
Internet service
Online security
Online backup
Device protection
Technical support
Streaming TV
Streaming movies
💳 Account & Billing
Contract type
Paperless billing
Payment method
Monthly charges
Total charges

The application provides:

🟢 Low Risk
🟠 Medium Risk
🔴 High Risk
Estimated churn probability
Business-oriented recommendation
🛠️ Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Joblib
Streamlit
Jupyter Notebook
Git & GitHub
📁 Project Structure
customer-churn-prediction/
│
├── app.py
├── customer_churn_model.pkl
├── customer_churn_prediction.ipynb
├── requirements.txt
├── WA_Fn-UseC_-Telco-Customer-Churn.csv
├── .gitignore
└── README.md
🚀 How to Run Locally
1. Clone the repository
git clone YOUR_GITHUB_REPOSITORY_URL
2. Navigate to the project folder
cd customer-churn-prediction
3. Install the required dependencies
pip install -r requirements.txt
4. Run the Streamlit application
streamlit run app.py

The application will open in your browser.

📌 Key Results

The final model achieved approximately:

80.55% Test Accuracy
84.21% Test ROC-AUC
56% Churn Recall
60% Churn F1-score
0.8459 Cross-Validation ROC-AUC

These results demonstrate that machine learning can be used to identify customers who may be at higher risk of leaving and help businesses develop targeted customer retention strategies.

💼 Business Use Case

Customer churn prediction can help businesses:

Identify customers who may be at risk of leaving
Prioritize retention efforts
Understand factors associated with customer churn
Improve customer engagement
Support data-driven business decisions

The application is designed to demonstrate how a machine learning model can be transformed into a simple business-facing tool.

⚠️ Disclaimer

The prediction generated by this application is an estimated probability produced by a machine learning model.

It should be considered a decision-support tool and not a guaranteed prediction of customer behavior.

🌐 Live Demo

https://syedjunaid-customer-churn.streamlit.app/

👨‍💻 Project

Customer Churn Prediction

An end-to-end Machine Learning project built using Python, Scikit-learn and Streamlit.

