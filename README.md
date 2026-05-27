## Live Demo

[Click Here to View the App](https://cred-card-fraud-detect.streamlit.app/)

---

## Project Overview

This project focuses on detecting fraudulent credit card transactions using Machine Learning techniques and interactive data visualizations.

The dashboard provides:
- Fraud analysis metrics
- Interactive visualizations
- ROC Curve evaluation
- Confusion Matrix analysis
- Model performance insights

The project uses a Random Forest Classifier trained on anonymized transaction data.

---

## Project Structure

```text
credit-card-fraud-detection/
│
├── app.py
├── fraud_model.pkl
├── requirements.txt
├── README.md
│
├── visuals/
│   ├── fraudvsvalid.png
│   ├── corr-mat.png
│   ├── roc.png
│   ├── confusion_matrix.png
```
---

## Run Locally

Clone repo: git clone YOUR_GITHUB_REPO_LINK
Install Dependencies: pip install -r requirements.txt
Run App: python -m streamlit run app.py
