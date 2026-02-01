# Customer Segmentation & Retention Analysis

## 📌 Project Overview

This project performs end-to-end Customer Segmentation and Retention Analysis using real-world transactional data.
The objective is to understand customer purchasing behavior, identify distinct customer segments,
analyze retention patterns, and predict customer churn to support data-driven business decisions.

The analysis focuses on translating customer behavior into actionable insights rather than just building models.

---

## 📊 Dataset

- Source: UCI Machine Learning Repository – Online Retail Dataset  
- Transactions from a UK-based online retailer  
- Records include invoices, products, quantities, prices, and customer IDs  
- Time period: 2010–2011  
- Dataset size: ~540K transactions, ~4.3K unique customers  

---

## 🧠 Methodology

1. **Exploratory Data Analysis (EDA)**
   - Missing value handling
   - Removal of cancelled transactions
   - Revenue distribution and customer activity analysis

2. **RFM Feature Engineering**
   - Recency: Days since last purchase
   - Frequency: Number of unique purchases
   - Monetary: Total customer spend

3. **Customer Segmentation**
   - RFM features scaled and clustered using K-Means
   - Customers grouped into 4 distinct behavioral segments

4. **Retention Analysis**
   - Monthly cohort-based retention analysis
   - Identification of early churn patterns and long-term retention trends

5. **Churn Prediction**
   - Churn defined as customer inactivity beyond a 90-day threshold
   - Random Forest classifier built using RFM and cluster features

---

## 🔍 Key Insights

- Recency is the strongest predictor of customer churn, contributing nearly 80% to the churn model.
- Customer segments exhibit clearly distinct purchasing behaviors, validating the RFM-based clustering approach.
- High-spending customers are not necessarily loyal; inactivity is a stronger churn signal than revenue.
- Cohort analysis reveals a sharp drop in retention after the first month, highlighting the importance of early engagement.

---

## 💡 Business Recommendations

- Prioritize retention strategies for customers showing increasing recency values rather than focusing only on high spenders.
- Design targeted engagement and win-back campaigns for high-risk customer segments.
- Improve onboarding and early customer experience to reduce first-month churn.
- Use churn prediction scores to proactively intervene before customers disengage.

---

## 🛠️ Tech Stack

- Python  
- Pandas, NumPy  
- Scikit-learn  
- Matplotlib, Seaborn  
- Jupyter Notebook  

---

## 📂 Project Structure

- notebooks/ – Analysis and modeling notebooks  
- data/ – Raw dataset  
- outputs/ – Processed data and model outputs  
- src/ – Reusable Python scripts  
