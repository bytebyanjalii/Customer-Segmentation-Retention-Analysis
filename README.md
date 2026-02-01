# 🚀 Customer Segmentation, Retention & Churn Analysis  
**End-to-End Data Science Project with Live Dashboard**

🔗 **Live Dashboard:**  
👉 h

---

## 📌 Project Overview

This project delivers an end-to-end **customer analytics solution** using real-world transactional data.  
It combines **customer segmentation**, **retention analysis**, and **churn prediction**, and presents insights through an **interactive Streamlit dashboard** designed for business stakeholders.

The focus is not just on modeling accuracy, but on **interpretability and actionable business insights**.

---

## 🎯 Business Objectives

- Understand customer purchasing behavior  
- Segment customers based on behavioral patterns  
- Identify early churn signals  
- Quantify revenue at risk due to churn  
- Enable data-driven retention strategies  

---

## 📊 Dataset

- **Source:** UCI Machine Learning Repository – Online Retail Dataset  
- **Domain:** UK-based online retail transactions  
- **Time Period:** 2010–2011  
- **Size:** ~540,000 transactions  

**Key fields include:**
- Invoice date
- Product details
- Quantity and price
- Customer ID

---

## 🧠 Methodology & Workflow

### 1️⃣ Exploratory Data Analysis (EDA)
- Removed cancelled transactions and invalid records  
- Handled missing customer IDs  
- Analyzed revenue distribution and customer activity  

### 2️⃣ RFM Feature Engineering
Each customer was represented using:
- **Recency:** Days since last purchase  
- **Frequency:** Number of transactions  
- **Monetary:** Total customer spend  

---

### 3️⃣ Customer Segmentation
- RFM features scaled and clustered using **K-Means**
- Customers grouped into **behavioral segments**
- Cluster quality validated using RFM distributions

---

### 4️⃣ Retention Analysis
- Defined churn based on inactivity threshold  
- Identified **critical churn window (60–90 days)**  
- Estimated **revenue at risk** from high-risk customers  

---

### 5️⃣ Churn Prediction
- Built a **Random Forest classifier**
- Features used:
  - Recency
  - Frequency
  - Monetary
  - Customer segment (cluster)
- Focused on **model explainability**, not just accuracy

---

### 6️⃣ Model Explainability
- Visualized feature importance
- Identified **Recency** as the strongest churn driver
- Translated ML outputs into business recommendations

---

## 📈 Key Insights

- **Recency explains ~80% of churn behavior**
- High spend does **not guarantee loyalty**
- Majority of churn occurs after **~90 days of inactivity**
- Certain segments contribute disproportionately to **revenue at risk**

---

## 💡 Business Recommendations

- Trigger retention campaigns based on **inactivity timing**, not just spend  
- Focus marketing on **high-risk, high-value segments**
- Improve early customer engagement to reduce first-month churn  
- Use churn scores for **proactive win-back campaigns**

---

## 🖥️ Interactive Dashboard

The project includes a **live Streamlit dashboard** with the following pages:

### 📊 Customer Segmentation Overview
- Customer distribution by segment  
- Revenue and RFM comparisons  

### 🚨 Churn Analysis
- Churn prediction insights  
- Feature importance visualization  

### 🔄 Retention Insights
- Revenue at risk analysis  
- Time-to-churn patterns  
- Actionable retention strategies  

### 🧠 Model Explainability
- Clear explanation of why customers churn  
- Business-friendly interpretation of ML models  

🔗 **Live App:**  
👉 https://YOUR-STREAMLIT-APP-LINK.streamlit.app  

---

## 🛠️ Tech Stack

- Python  
- Pandas, NumPy  
- Scikit-learn  
- Matplotlib, Seaborn, Plotly  
- Streamlit  
- Jupyter Notebook  

---

## 📂 Project Structure

