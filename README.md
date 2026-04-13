# 🚨 Crime Rate Pattern Analysis

## 📌 Overview
This project focuses on analyzing crime patterns across different states using data analysis and machine learning techniques. The main objective is to understand crime trends, identify high-crime regions, and predict future crime rates based on historical data.

The dataset includes state-wise crime statistics for multiple years along with population and chargesheeting rate. The project involves data preprocessing, exploratory data analysis (EDA), and predictive modeling using Linear Regression.

An interactive dashboard is also developed using Streamlit to visualize crime trends and allow users to explore data dynamically.

---

## 🎯 Objectives
- Analyze crime trends over multiple years
- Identify states with high and low crime rates
- Study the relationship between population and crime
- Evaluate chargesheet rate effectiveness
- Predict future crime trends using machine learning

---

## ⚙️ Technologies Used
- Python (Pandas, Matplotlib, Scikit-learn)
- SQL (MySQL)
- Streamlit (for dashboard)
- GitHub (for version control)

---

## 📊 Key Features
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering (Average Crime, Crime Growth, Crime per Population)
- Linear Regression model for prediction
- Interactive Streamlit dashboard with filters

---

## 🤖 Machine Learning
A Linear Regression model is used to predict crime counts based on:
- Previous year crime data
- Population
- Chargesheet rate

The model achieved high accuracy with an R² score of approximately 0.96, indicating strong predictive performance.

---

## 📁 Project Files
- `app.py` → Streamlit dashboard
- `analysis.py` → Data analysis and ML code
- `crime_sql.sql` → SQL queries
- `crime_data.csv` → Dataset
- `report.docx` → Project documentation
- `requirements.txt` → Dependencies

---

## 🌐 How to Run
```bash
streamlit run app.py
