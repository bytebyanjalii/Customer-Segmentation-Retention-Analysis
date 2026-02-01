import streamlit as st

st.set_page_config(
    page_title="Customer Segmentation & Retention Dashboard",
    layout="wide"
)

st.title("📊 Customer Segmentation & Retention Analysis")

st.markdown("""
This dashboard provides insights into customer behavior, churn risk,
and retention patterns using transactional data.

Use the navigation menu on the left to explore:
- Customer Segmentation
- Churn Analysis
- Retention Insights
""")