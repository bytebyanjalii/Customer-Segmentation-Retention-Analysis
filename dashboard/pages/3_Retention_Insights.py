import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_loader import load_rfm

st.title("🔄 Retention Insights & Business Actions")

rfm = load_rfm()

# ---------------- Churn Definition ----------------
CHURN_THRESHOLD = 90
rfm["Churn"] = (rfm["Recency"] > CHURN_THRESHOLD).astype(int)

# ---------------- High Risk Customers ----------------
st.subheader("🚨 High-Risk Customers (Likely to Churn)")

high_risk = rfm[(rfm["Recency"] > CHURN_THRESHOLD) & (rfm["Frequency"] <= 2)]

col1, col2, col3 = st.columns(3)
col1.metric("High-Risk Customers", len(high_risk))
col2.metric("Avg Recency (Days)", round(high_risk["Recency"].mean(), 1))
col3.metric("Avg Spend", f"{high_risk['Monetary'].mean():,.0f}")

# ---------------- Revenue at Risk ----------------
st.divider()
st.subheader("💰 Revenue at Risk")

revenue_at_risk = high_risk["Monetary"].sum()
total_revenue = rfm["Monetary"].sum()

st.metric(
    "Revenue at Risk",
    f"{revenue_at_risk:,.2f}",
    delta=f"{(revenue_at_risk / total_revenue) * 100:.1f}% of total revenue",
)

# ---------------- Time-to-Churn Distribution ----------------
st.divider()
st.subheader("⏱ Time Since Last Purchase (Churn Risk Curve)")

fig_time = px.histogram(
    rfm,
    x="Recency",
    color="Churn",
    nbins=40,
    title="Distribution of Recency (Days Since Last Purchase)",
    labels={"Recency": "Days Since Last Purchase"},
)

st.plotly_chart(fig_time, use_container_width=True)

st.info(
    "📌 Insight: Most customers who churn do so after ~90 days of inactivity. "
    "This window represents a critical intervention period."
)

# ---------------- Cluster-wise Risk ----------------
st.divider()
st.subheader("📊 Revenue at Risk by Customer Segment")

risk_cluster = (
    high_risk.groupby("Cluster")["Monetary"]
    .sum()
    .reset_index()
)

fig_cluster = px.bar(
    risk_cluster,
    x="Cluster",
    y="Monetary",
    color="Cluster",
    title="Revenue at Risk by Customer Segment",
)

st.plotly_chart(fig_cluster, use_container_width=True)

st.info(
    "📌 Insight: Certain customer segments contribute disproportionately "
    "to revenue at risk, making segmentation critical for targeted retention."
)

# ---------------- Business Recommendations ----------------
st.divider()
st.subheader("📌 Actionable Retention Strategies")

st.markdown("""
### 🔵 High-Value & Recently Active Customers
- Loyalty rewards and VIP benefits  
- Personalized product recommendations  
- Early access to new collections  

### 🟠 Medium-Value Customers
- Discount bundles  
- Reminder emails based on browsing behavior  
- Seasonal promotions  

### 🔴 At-Risk Customers (High Recency)
- Time-bound win-back campaigns  
- Re-engagement emails after 60 days  
- Incentives to trigger next purchase  

### ⚫ Low-Value / Long-Churned Customers
- Reduce paid marketing spend  
- Automated, low-cost email flows  
""")

st.success(
    "✅ Business Impact: Intervening during the 60–90 day inactivity window can "
    "significantly reduce churn while preserving high-value customer revenue."
)
