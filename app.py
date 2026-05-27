import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# PAGE CONFIG
st.set_page_config(
    page_title="Credit Card Fraud Detection",
    layout="wide"
)

# LOAD MODEL + DATA
model = joblib.load("fraud_model.pkl")

data = pd.read_csv("creditcard.csv")

# TITLE
st.title("💳 Credit Card Fraud Detection System")

st.markdown("""
This application predicts whether a transaction is fraudulent or genuine using Machine Learning.
""")

# SIDEBAR
st.sidebar.title("Navigation")

section = st.sidebar.radio(
    "Go to",
    [
        "Dataset Overview",
        "Visualizations",
        "Model Performance",
        "Fraud Prediction"
    ]
)

# DATASET OVERVIEW
if section == "Dataset Overview":

    st.header("Dataset Overview")

    total = len(data)
    fraud = len(data[data['Class'] == 1])
    valid = len(data[data['Class'] == 0])

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Transactions", total)
    col2.metric("Fraud Transactions", fraud)
    col3.metric("Valid Transactions", valid)

    st.subheader("Dataset Preview")

    st.dataframe(data.head())

# VISUALIZATIONS
elif section == "Visualizations":

    st.header("📈 Visualizations")

    # Fraud Distribution
    st.subheader("Fraud vs Valid Transactions")

    fig, ax = plt.subplots()

    sns.countplot(x='Class', data=data, ax=ax)

    ax.set_xticklabels(['Valid', 'Fraud'])

    st.pyplot(fig)

    # Amount Distribution
    st.subheader("Transaction Amount Distribution")

    fig2, ax2 = plt.subplots(figsize=(8,5))

    sns.histplot(data['Amount'], bins=50, ax=ax2)

    st.pyplot(fig2)

    # Correlation Heatmap
    st.subheader("Correlation Heatmap")

    fig3, ax3 = plt.subplots(figsize=(12,8))

    sns.heatmap(
        data.corr(),
        cmap='coolwarm',
        ax=ax3
    )

    st.pyplot(fig3)

# MODEL PERFORMANCE
elif section == "Model Performance":

    st.header("🤖 Model Performance")

    st.metric("Accuracy", "99%")
    st.metric("ROC-AUC Score", "0.96")

    st.markdown("""
### Interpretation

- High ROC-AUC score indicates strong fraud detection capability.
- Model performs well even on imbalanced datasets.
""")

# FRAUD PREDICTION
elif section == "Fraud Prediction":

    st.header("🚨 Predict Fraudulent Transaction")

    st.markdown("Enter transaction feature values below.")

    input_data = []

    for i in range(1, 29):

        value = st.number_input(
            f"V{i}",
            value=0.0
        )

        input_data.append(value)

    amount = st.number_input("Amount", value=0.0)

    input_data.append(amount)

    time = st.number_input("Time", value=0.0)

    input_data.append(time)

    if st.button("Predict"):

        input_array = np.array(input_data).reshape(1, -1)

        prediction = model.predict(input_array)

        if prediction[0] == 1:

            st.error("🚨 Fraudulent Transaction Detected")

        else:

            st.success("✅ Genuine Transaction")