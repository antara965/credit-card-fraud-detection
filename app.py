import streamlit as st
import pandas as pd

# PAGE CONFIG
st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳",
    layout="wide"
)

# LOAD DATA
data = pd.read_csv("creditcard.csv")

st.title("💳 Credit Card Fraud Detection Dashboard")

st.markdown("""
This dashboard analyzes fraudulent and genuine credit card transactions using Machine Learning and Data Analytics.
""")

# SIDEBAR
st.sidebar.title("Navigation")

section = st.sidebar.radio(
    "Go To",
    [
        "Dataset Overview",
        "Visualizations",
        "Model Performance",
        "About Project"
    ]
)

if section == "Dataset Overview":

    st.header("Dataset Overview")

    total_transactions = len(data)
    fraud_transactions = len(data[data['Class'] == 1])
    valid_transactions = len(data[data['Class'] == 0])

    fraud_percentage = (
        fraud_transactions / total_transactions
    ) * 100

    # METRICS

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Transactions",
        f"{total_transactions:,}"
    )

    col2.metric(
        "Fraud Transactions",
        fraud_transactions
    )

    col3.metric(
        "Valid Transactions",
        valid_transactions
    )

    col4.metric(
        "Fraud Percentage",
        f"{fraud_percentage:.4f}%"
    )

    st.divider()

    # DATA PREVIEW

    st.subheader("Dataset Preview")

    st.dataframe(data.head())

    st.divider()

    # DATASET INFO

    st.subheader("Dataset Information")

    st.write(f"Number of Rows: {data.shape[0]}")
    st.write(f"Number of Columns: {data.shape[1]}")

elif section == "Visualizations":

    st.header("Visualizations")

    st.markdown("""
    These visualizations help analyze transaction patterns, fraud distribution, and model performance.
    """)

    st.divider()

    # FRAUD VS VALID

    st.subheader("1️⃣ Fraud vs Valid Transactions")

    st.image(
        "visuals/fraudvsvalid.png",
        use_container_width=True
    )

    st.markdown("""
    **Observation:**  
    Fraudulent transactions are significantly lower than genuine transactions, showing severe class imbalance in the dataset.
    """)

    st.divider()

    # CORRELATION MATRIX

    st.subheader("2️⃣ Correlation Heatmap")

    st.image(
        "visuals/corr-mat.png",
        use_container_width=True
    )

    st.markdown("""
    **Observation:**  
    The heatmap shows relationships between different features and helps identify highly correlated variables.
    """)

    st.divider()

    # ROC CURVE

    st.subheader("3️⃣ ROC Curve")

    st.image(
        "visuals/roc.png",
        use_container_width=True
    )

    st.markdown("""
    **Observation:**  
    The ROC-AUC score of 0.96 indicates excellent fraud detection capability with low false positive rates.
    """)

    st.divider()

    # CONFUSION MATRIX

    st.subheader("4️⃣ Confusion Matrix")

    st.image(
        "visuals/confusion_matrix.png",
        use_container_width=True
    )

    st.markdown("""
    **Observation:**  
    The confusion matrix shows that the model correctly classifies most transactions with very few misclassifications.
    """)

elif section == "Model Performance":

    st.header("Model Performance")

    st.markdown("""
    Performance metrics of the Random Forest Classifier used for fraud detection.
    """)

    st.divider()

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Accuracy",
        "99%"
    )

    col2.metric(
        "ROC-AUC Score",
        "0.96"
    )

    col3.metric(
        "Recall",
        "91%"
    )

    st.divider()

    st.subheader("Interpretation")

    st.markdown("""
    - The model achieves very high accuracy in identifying fraudulent transactions.
    - A ROC-AUC score of 0.96 indicates strong classification capability.
    - High recall means the model successfully detects most fraud cases.
    - Random Forest performs well on imbalanced classification problems.
    """)

elif section == "About Project":

    st.header("About Project")

    st.markdown("""
    ### 💳 Credit Card Fraud Detection System

    This project focuses on detecting fraudulent credit card transactions using Machine Learning techniques.

    The dataset contains anonymized transaction information and highly imbalanced fraud data.

    ### Objective

    The main objective of this project is to:
    - Detect fraudulent transactions accurately
    - Minimize false positives
    - Analyze fraud patterns using data visualization

    ### Technologies Used

    - Python
    - Pandas
    - NumPy
    - Matplotlib
    - Seaborn
    - Scikit-learn
    - Streamlit

    ### Machine Learning Model

    - Random Forest Classifier

    ### Key Features

    - Fraud analysis dashboard
    - Interactive visualizations
    - ROC Curve analysis
    - Confusion Matrix evaluation
    - Dataset overview metrics

    ### Model Highlights

    - Accuracy: 99%
    - ROC-AUC Score: 0.96
    - Strong fraud detection capability
    """)