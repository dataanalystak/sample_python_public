import streamlit as st
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(page_title="Home Loan EMI Calculator", page_icon="🏠", layout="centered")

# --- Custom CSS ---
st.markdown("""
    <style>
        .main {
            background-color: #f0f9ff;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            border-radius: 8px;
            height: 3em;
            width: 100%;
        }
        .stNumberInput>div>div>input {
            font-size: 18px;
            color: #003366;
        }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<h1 style='color: #2E8B57;'>🏡 Home Loan EMI Calculator</h1>", unsafe_allow_html=True)
st.markdown("Estimate your monthly payments for a home loan using the inputs below.")

# --- Inputs ---
st.subheader("🔢 Loan Details")
loan_amount = st.number_input("🏦 Loan Amount (₹)", min_value=0.0, value=500000.0, step=10000.0, format="%.2f")
interest_rate = st.number_input("📈 Annual Interest Rate (%)", min_value=0.0, value=8.5, step=0.1, format="%.2f")
loan_tenure_years = st.number_input("📅 Loan Tenure (Years)", min_value=1, value=20, step=1)

# --- EMI Calculation Function ---
def calculate_emi(P, R, N):
    monthly_rate = R / (12 * 100)
    num_payments = N * 12
    if monthly_rate == 0:
        return P / num_payments
    emi = P * monthly_rate * ((1 + monthly_rate) ** num_payments) / (((1 + monthly_rate) ** num_payments) - 1)
    return emi

# --- Calculate & Display ---
if st.button("💰 Calculate EMI"):
    emi = calculate_emi(loan_amount, interest_rate, loan_tenure_years)
    total_payment = emi * loan_tenure_years * 12
    total_interest = total_payment - loan_amount

    # Display Results
    st.success("✅ Calculation Complete!")
    st.markdown(f"""
        ### 📊 Loan Summary
        - **Monthly EMI:** ₹{emi:,.2f}
        - **Total Payment:** ₹{total_payment:,.2f}
        - **Total Interest:** ₹{total_interest:,.2f}
    """)

    # --- Pie Chart ---
    fig, ax = plt.subplots()
    labels = 'Principal Amount', 'Total Interest'
    sizes = [loan_amount, total_interest]
    colors = ['#4CAF50', '#FF6F61']
    explode = (0, 0.1)

    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90,
           colors=colors, explode=explode, shadow=True)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig)

    st.info("Tip: You can reduce your EMI by increasing the tenure or reducing the interest rate.")
