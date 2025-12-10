# Filename: app.py
import streamlit as st
import requests

# ----------------- Page Config -----------------
st.set_page_config(page_title="Credit Card Fraud Detection", layout="wide")

# Your deployed AWS API Gateway endpoint
API_URL = "https://zlvf4i1s97.execute-api.eu-north-1.amazonaws.com/prod/predict"

# ----------------- Header -----------------
st.title("Credit Card Fraud Detection System")
st.write("Enter transaction details below and get real-time prediction from AWS SageMaker.")

# ----------------- Manual Input -----------------
st.subheader("Transaction Input")

input_data = {}
input_data['Time'] = st.number_input("Time", value=0.0)

for i in range(1, 29):
    input_data[f'V{i}'] = st.number_input(f"V{i}", value=0.0)

input_data['Amount'] = st.number_input("Amount", value=0.0)

# ----------------- Predict Button -----------------
if st.button("Predict"):
    with st.spinner("Getting prediction from AWS..."):
        try:
            response = requests.post(API_URL, json=input_data)
            result = response.json()

            if "prediction" in result:
                # Remove any trailing newline or spaces
                score = float(result["prediction"].strip())
                if score > 0.5:
                    st.error(f"⚠️ Fraud Detected! (score = {score:.4f})")
                else:
                    st.success(f"✅ Transaction is Safe (score = {score:.4f})")
            else:
                st.warning(result)

        except Exception as e:
            st.error(f"Error: {str(e)}")

# ----------------- Footer -----------------
st.markdown("---")
st.markdown("""
<p style="text-align:center; color:gray; font-size:14px;">
Developed by <b>Chaitanya Jamdar</b><br>
LinkedIn: 
<a href="https://www.linkedin.com/in/chaitanya-jamdar-13706625b/" target="_blank">
Chaitanya Jamdar
</a><br>
Email: <a href="mailto:jamdarchaitanya127@gmail.com">jamdarchaitanya127@gmail.com</a>
</p>
""", unsafe_allow_html=True)
