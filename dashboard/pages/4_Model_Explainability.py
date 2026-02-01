import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

from utils.data_loader import load_rfm

st.title("🧠 Model Explainability – Why Customers Churn")

# ---------------- Load Data ----------------
rfm = load_rfm()

# Define churn (same logic as model)
rfm["Churn"] = (rfm["Recency"] > 90).astype(int)

# ---------------- Train Simple Explainable Model ----------------
from sklearn.ensemble import RandomForestClassifier

features = ["Recency", "Frequency", "Monetary", "Cluster"]
X = rfm[features]
y = rfm["Churn"]

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
model.fit(X, y)

# ---------------- Feature Importance ----------------
importance = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
}).sort_values(by="Importance", ascending=False)

st.subheader("🔍 Feature Importance in Churn Prediction")

fig = px.bar(
    importance,
    x="Importance",
    y="Feature",
    orientation="h",
    title="Which Factors Drive Customer Churn?",
)

st.plotly_chart(fig, use_container_width=True)

# ---------------- Interpretation ----------------
st.divider()
st.subheader("📌 Key Insights")

top_feature = importance.iloc[0]["Feature"]

st.markdown(f"""
### 🥇 Most Important Factor: **{top_feature}**

**What this means:**
- Customers are far more likely to churn based on **inactivity duration** than spending amount.
- Revenue alone is a weak loyalty indicator.

### 🧠 Business Interpretation
- A customer who spent a lot **can still churn** if they stop purchasing.
- Early inactivity signals matter more than historical value.

### 🎯 Recommended Actions
- Trigger retention campaigns based on **Recency thresholds**
- Stop relying only on revenue-based segmentation
- Monitor churn risk weekly using inactivity signals
""")

st.success(
    "✅ Takeaway: Churn prevention is a timing problem, not a discount problem."
)
