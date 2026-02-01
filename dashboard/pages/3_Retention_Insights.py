import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_loader import load_rfm

st.title("🔄 Retention Insights & Business Actions")

rfm = load_rfm()

# ---------------- Churn Definition ----------------
rfm["Churn"] = (rfm["Recency"] > 90).astype(int)

# ---------------- High Risk Customers ----------------
st.subheader("🚨 High-Risk Customers (Likely to Churn)")

high_risk = rfm[(rfm["Recency"] > 90) & (rfm["Frequency"] <= 2)]

st.metric("High-Risk Customers", len(high_risk))

# ---------------- Revenue at Risk ----------------
revenue_at_risk = high_risk["Monetary"].sum()

st.metric("💰 Revenue at Risk", f"{revenue_at_risk:,.2f}")

st.divider()

# ---------------- Cluster-wise Risk ----------------
st.subheader("Revenue at Risk by Segment")

risk_cluster = (
    high_risk.groupby("Cluster")["Monetary"]
    .sum()
    .reset_index()
)

fig1 = px.bar(
    risk_cluster,
    x="Cluster",
    y="Monetary",
    color="Cluster",
    title="Revenue at Risk by Customer Segment"
)

st.plotly_chart(fig1, use_container_width=True)

# ---------------- Business Recommendations ----------------
st.subheader("📌 Actionable Retention Strategies")

st.markdown("""
### 🔵 High-Value Customers (Low Recency, High Monetary)
- Offer **loyalty rewards**
- Early access to premium products
- Personalized recommendations

### 🟠 Medium-Value Customers
- Discount bundles
- Email reminders
- Seasonal promotions

### 🔴 At-Risk Customers (High Recency)
- Win-back campaigns
- Limited-time offers
- Re-engagement emails

### ⚫ Low-Value / Churned Customers
- Reduce marketing spend
- Automated low-cost retention
""")

st.success(
    "✅ Business Impact: Targeting the top 20% high-risk customers can significantly "
    "reduce churn while protecting the majority of revenue."
)