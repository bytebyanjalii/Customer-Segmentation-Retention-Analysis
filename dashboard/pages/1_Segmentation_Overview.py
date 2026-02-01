import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_loader import load_rfm

st.title("🧩 Customer Segmentation Overview")

rfm = load_rfm()

# ---------------- KPIs ----------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Customers", rfm.shape[0])
col2.metric("Active Customers", (rfm['Recency'] <= 90).sum())
col3.metric("Churned Customers", (rfm['Recency'] > 90).sum())
col4.metric("Avg Revenue / Customer", round(rfm['Monetary'].mean(), 2))

st.divider()

# ---------------- Customer Distribution ----------------
st.subheader("Customer Distribution by Segment")

cluster_counts = rfm['Cluster'].value_counts().reset_index()
cluster_counts.columns = ['Cluster', 'Customers']

fig1 = px.bar(
    cluster_counts,
    x="Cluster",
    y="Customers",
    color="Cluster",
    title="Customers per Segment"
)
st.plotly_chart(fig1, use_container_width=True)

# ---------------- Frequency vs Monetary ----------------
st.subheader("Customer Value Distribution")

fig2 = px.scatter(
    rfm,
    x="Frequency",
    y="Monetary",
    color="Cluster",
    title="Frequency vs Monetary Value by Segment",
    hover_data=["Recency"]
)
st.plotly_chart(fig2, use_container_width=True)

# ---------------- Average RFM ----------------
st.subheader("Average RFM Metrics by Segment")

rfm_avg = rfm.groupby("Cluster")[['Recency', 'Frequency', 'Monetary']].mean().reset_index()

fig3 = px.bar(
    rfm_avg.melt(id_vars="Cluster"),
    x="Cluster",
    y="value",
    color="variable",
    barmode="group",
    title="Average RFM Metrics per Segment"
)
st.plotly_chart(fig3, use_container_width=True)