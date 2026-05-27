import streamlit as st

st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳",
    layout="wide"
)

st.title("💳 Credit Card Fraud Detection Dashboard")

st.markdown("""
This dashboard analyzes fraudulent and genuine credit card transactions using Machine Learning and Data Analytics.
""")

st.sidebar.title("📌 Navigation")

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

    st.header("📊 Dataset Overview")

    total_transactions = 284807
    fraud_transactions = 492
    valid_transactions = 284315

    fraud_percentage = (
        fraud_transactions / total_transactions
    ) * 100

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

    st.subheader("📌 Dataset Information")

    st.write("Number of Rows: 284,807")
    st.write("Number of Columns: 31")

    st.markdown("""
    ### Dataset Description

    The dataset contains anonymized credit card transactions made by European cardholders.

    - Features V1 to V28 are PCA transformed features
    - `Amount` represents transaction amount
    - `Class` represents:
        - 0 → Genuine Transaction
        - 1 → Fraudulent Transaction
    """)

elif section == "Visualizations":

    st.header("📈 Visualizations")

    st.markdown("""
    These visualizations help analyze fraud distribution and model performance.
    """)

    st.divider()

    st.subheader("1️⃣ Fraud vs Valid Transactions")

    st.image(
        "visuals/fraudvsvalid.png",
        use_container_width=True
    )

    st.markdown("""
    **Observation:**  
    Fraudulent transactions are significantly lower than genuine transactions, indicating severe class imbalance.
    """)

    st.divider()

    st.subheader("2️⃣ Correlation Heatmap")

    st.image(
        "visuals/corr-mat.png",
        use_container_width=True
    )

    st.markdown("""
    **Observation:**  
    The heatmap highlights relationships between different transaction features.
    """)

    st.divider()

    st.subheader("3️⃣ ROC Curve")

    st.image(
        "visuals/roc.png",
        use_container_width=True
    )

    st.markdown("""
    **Observation:**  
    The ROC-AUC score of 0.96 indicates excellent fraud detection capability.
    """)

    st.divider()

    st.subheader("4️⃣ Confusion Matrix")

    st.image(
        "visuals/confusion_matrix.png",
        use_container_width=True
    )

    st.markdown("""
    **Observation:**  
    The model correctly classifies most transactions with very few misclassifications.
    """)

elif section == "Model Performance":

    st.header("🤖 Model Performance")

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

    st.subheader("📌 Interpretation")

    st.markdown("""
    - High accuracy indicates strong fraud classification performance
    - ROC-AUC score of 0.96 shows excellent separation capability
    - High recall means most fraud cases are successfully detected
    - Random Forest performs effectively on imbalanced datasets
    """)

elif section == "About Project":

    st.header("📌 About Project")

    st.markdown("""
    ### 💳 Credit Card Fraud Detection System

    This project focuses on identifying fraudulent credit card transactions using Machine Learning techniques.

    ### 🎯 Objective

    - Detect fraudulent transactions accurately
    - Minimize false positives
    - Analyze fraud patterns using visualizations

    ### 🛠️ Technologies Used

    - Python
    - Pandas
    - NumPy
    - Matplotlib
    - Seaborn
    - Scikit-learn
    - Streamlit

    ### 🤖 Machine Learning Model

    - Random Forest Classifier

    ### 📈 Model Highlights

    - Accuracy: 99%
    - ROC-AUC Score: 0.96
    - Strong fraud detection capability
    """)