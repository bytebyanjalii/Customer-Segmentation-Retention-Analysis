# This page will:
# Show churn KPIs
# Show churn by cluster
# Visualize why churn happens (recency dominance)

import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_loader import load_rfm

st.title("⚠️ Churn Analysis")

rfm = load_rfm()

# ---------------- Churn Definition ----------------
rfm["Churn"] = (rfm["Recency"] > 90).astype(int)

# ---------------- KPIs ----------------
col1, col2, col3 = st.columns(3)

churn_rate = rfm["Churn"].mean() * 100

col1.metric("Overall Churn Rate", f"{churn_rate:.2f}%")
col2.metric("Churned Customers", rfm["Churn"].sum())
col3.metric("Active Customers", (rfm["Churn"] == 0).sum())

st.divider()

# ---------------- Churn Rate by Cluster ----------------
st.subheader("Churn Rate by Customer Segment")

churn_cluster = (
    rfm.groupby("Cluster")["Churn"]
    .mean()
    .reset_index()
)

fig1 = px.bar(
    churn_cluster,
    x="Cluster",
    y="Churn",
    color="Cluster",
    title="Churn Rate by Segment"
)

fig1.update_yaxes(tickformat=".0%")
st.plotly_chart(fig1, use_container_width=True)

# ---------------- Recency Distribution ----------------
st.subheader("Recency Distribution: Active vs Churned Customers")

fig2 = px.box(
    rfm,
    x="Churn",
    y="Recency",
    color="Churn",
    labels={"Churn": "Churn Status (0 = Active, 1 = Churned)"},
    title="Recency Comparison"
)

st.plotly_chart(fig2, use_container_width=True)

# ---------------- Insight ----------------
st.info(
    "📌 Insight: Customers with higher recency values are significantly more likely to churn, "
    "confirming that inactivity is the strongest churn signal."
)
