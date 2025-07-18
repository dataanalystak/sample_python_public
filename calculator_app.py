import streamlit as st
import matplotlib.pyplot as plt

# --- Page Config ---
st.set_page_config(page_title="Home Loan Calculator 💰", page_icon="💵", layout="centered")

# --- Dark Blue Theme with Watermark ---
st.markdown("""
    <style>
        .stApp {
            background-color: #001f3f;
            background-image: url('https://upload.wikimedia.org/wikipedia/commons/6/6b/Dollar_sign_green.svg');
            background-repeat: no-repeat;
            background-position: center;
            background-size: 250px;
            opacity: 0.98;
        }

        h1, h2, h3, h4, h5, h6, p, label, div, span {
            color: #ffffff !important;
        }

        .stNumberInput>div>div>input {
            background-color: #003366;
            color: #ffffff;
            border: 1px solid #0099ff;
        }

        .stButton>button {
            background-color: #0099ff;
            color: white;
            font-size: 16px;
            border-radius: 10px;
            padding: 10px 20px;
            border: none;
        }

        .css-1kyxreq {
            background-color: transparent !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<h1 style='text-align:center;'>💵 Home Loan EMI Calculator</h1>", unsafe_allow_html=True)
st.write("Use this tool to calculate your monthly mortgage payments.")

# --- Inputs ---
st.subheader("🔢 Loan Details")
loan_amount = st.number_input("🏦 Loan Amount ($)", min_value=0.0, value=250000.0, step=5000.0, format="%.2f")
interest_rate = st.number_input("📈 Interest Rate (% per year)", min_value=0.0, value=6.5, step=0.1, format="%.2f")
loan_tenure = st.number_input("📅 Loan Tenure (Years)", min_value=1, value=30, step=1)

# --- EMI Calculation ---
def calculate_emi(P, R, N):
    monthly_rate = R / (12 * 100)
    num_payments = N * 12
    if monthly_rate == 0:
        return P / num_payments
    emi = P * monthly_rate * ((1 + monthly_rate)**num_payments) / ((1 + monthly_rate)**num_payments - 1)
    return emi

# --- Button ---
if st.button("💰 Calculate EMI"):
    emi = calculate_emi(loan_amount, interest_rate, loan_tenure)
    total_payment = emi * loan_tenure * 12
    total_interest = total_payment - loan_amount

    st.success("✅ Calculation Complete!")

    st.markdown(f"""
        ### 📊 Loan Summary
        - **Monthly EMI:** ${emi:,.2f}
        - **Total Payment:** ${total_payment:,.2f}
        - **Total Interest:** ${total_interest:,.2f}
    """)

    # --- Pie Chart ---
    fig, ax = plt.subplots()
    labels = ['Principal', 'Interest']
    values = [loan_amount, total_interest]
    colors = ['#0074D9', '#39CCCC']
    explode = (0, 0.1)
    ax.pie(values, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90, explode=explode, shadow=True)
    ax.axis('equal')
    st.pyplot(fig)


#info line
    st.info("💡 Tip: Lower interest or longer tenure can reduce your monthly EMI.")
