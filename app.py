import streamlit as st

st.set_page_config(
    page_title="Datvest Investment Intelligence",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Datvest Investment Intelligence")
st.write("AI-powered investment research and portfolio analysis.")

st.divider()

st.header("Welcome")

st.write(
    """
    This platform is being developed to assist investment professionals
    with financial analysis, risk assessment, valuation and portfolio research.
    """
)

st.info("🚧 Project under development")

st.sidebar.title("Navigation")

option = st.sidebar.selectbox(
    "Choose a module",
    [
        "Dashboard",
        "Company Analysis",
        "Risk Analysis",
        "Valuation",
        "Portfolio Analysis",
        "AI Research Assistant"
    ]
)

st.subheader(option)

st.write("This module will be developed next.")
