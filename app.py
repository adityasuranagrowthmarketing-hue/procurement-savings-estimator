import streamlit as st

st.set_page_config(
    page_title="Procurement Savings Estimator",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------- STYLE FIX ----------

st.markdown("""
<style>

/* Force selected dropdown value to black */
div[data-baseweb="select"] > div {
    color: black !important;
}

/* Button styling */
.stButton > button {
background-color:#C9F1F7 !important;
color:black !important;
border:none !important;
font-weight:600;
padding:12px 26px;
border-radius:8px;
font-size:16px;
}

.stButton > button:hover {
background-color:#C9F1F7 !important;
color:black !important;
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------

st.title("Estimate Hidden Procurement Savings")

st.markdown(
"Answer a few simple questions to estimate potential procurement savings in **under 10 seconds**."
)

st.divider()

# ---------- INPUTS ----------

spend = st.selectbox(
"Annual Procurement Spend",
["<$50M", "$50M-$250M", "$250M-$1B", "$1B+"]
)

suppliers = st.selectbox(
"Number Of Suppliers",
["<100", "100-500", "500-2000", "2000+"]
)

erp = st.selectbox(
"ERP System",
["SAP", "Coupa", "Oracle", "Other"]
)

automation = st.selectbox(
"Procurement Automation Level",
["Mostly Manual", "Partially Automated", "Highly Automated"]
)

st.divider()

# ---------- CALCULATE ----------

if st.button("Calculate Potential Savings"):

    leakage_rate = 0.03

    if automation == "Mostly Manual":
        leakage_rate += 0.02
    elif automation == "Highly Automated":
        leakage_rate -= 0.015

    if suppliers == "100-500":
        leakage_rate += 0.005
    elif suppliers == "500-2000":
        leakage_rate += 0.01
    elif suppliers == "2000+":
        leakage_rate += 0.02

    spend_values = {
        "<$50M": 50_000_000,
        "$50M-$250M": 250_000_000,
        "$250M-$1B": 1_000_000_000,
        "$1B+": 3_000_000_000
    }

    estimated_spend = spend_values[spend]

    savings = estimated_spend * leakage_rate

    low_range = savings * 0.85
    high_range = savings * 1.15

    # ---------- RESULTS ----------

    st.subheader("Estimated Annual Procurement Savings Opportunity")

    st.markdown(f"## £{savings:,.0f} per year")

    st.markdown(
        f"Typical range: **£{low_range:,.0f} – £{high_range:,.0f}**"
    )

    st.success(
        "Procurement teams with similar supplier complexity frequently uncover multi-million pound savings during supplier contract audits."
    )

    st.info(
        "Magentic's AI procurement agents analyse supplier contracts, invoices and ERP data to detect pricing inconsistencies, missed rebates and contract compliance gaps."
    )

    st.divider()

    st.markdown("### See How Magentic AI Agents Deliver Procurement Savings")

    # ---------- FINAL CTA ----------

    st.markdown("""
<div style="text-align:center;margin-top:25px;">
<a href="https://www.magentic.com" target="_blank">
<button style="
background-color:#C9F1F7;
color:black;
border:none;
padding:14px 28px;
font-size:16px;
font-weight:600;
border-radius:8px;
cursor:pointer;">
See How <b>Magentic</b> Unlocks Procurement Savings
</button>
</a>
</div>
""", unsafe_allow_html=True)
