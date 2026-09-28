import streamlit as st
import pandas as pd

from company_analysis import analyze_company


st.set_page_config(
    page_title="Datvest Investment Intelligence",
    page_icon="📊",
    layout="wide"
)


# ==========================================
# HEADER
# ==========================================

st.title("📊 Datvest Investment Intelligence")

st.caption(
    "Financial analysis and investment research platform"
)


# ==========================================
# SIDEBAR
# ==========================================

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


# ==========================================
# DASHBOARD
# ==========================================

if option == "Dashboard":

    st.header("Investment Intelligence Dashboard")

    st.write(
        """
        Welcome to the investment research platform.

        The system is being developed to support:
        financial analysis, risk assessment, valuation,
        portfolio analysis and investment research.
        """
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    col1.metric("Modules", "6")
    col2.metric("Status", "Development")
    col3.metric("Analysis Engine", "Active")

    st.info(
        "Select Company Analysis from the sidebar to begin."
    )


# ==========================================
# COMPANY ANALYSIS
# ==========================================

elif option == "Company Analysis":

    st.header("🏢 Company Analysis")

    st.write(
        """
        Enter historical financial information for a company.
        The system will calculate growth and financial ratios.
        """
    )

    company_name = st.text_input(
        "Company Name",
        "Example Holdings"
    )

    st.subheader("Historical Financial Data")

    data = pd.DataFrame({
        "Year": [2022, 2023, 2024, 2025],
        "Revenue": [100, 120, 140, 165],
        "Net Income": [10, 12, 15, 19],
        "Total Assets": [80, 90, 105, 120],
        "Equity": [40, 45, 52, 60],
        "Debt": [20, 22, 25, 27],
        "Current Assets": [30, 35, 40, 45],
        "Current Liabilities": [15, 17, 20, 22]
    })

    edited_data = st.data_editor(
        data,
        num_rows="fixed",
        hide_index=True,
        width="stretch"
    )

    if st.button("Analyze Company"):

        results = analyze_company(edited_data)

        st.divider()

        st.subheader(
            f"📈 {company_name} — Investment Analysis"
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Revenue Growth",
            f"{results['Revenue Growth']:.2%}"
        )

        col2.metric(
            "Earnings Growth",
            f"{results['Earnings Growth']:.2%}"
        )

        col3.metric(
            "Profit Margin",
            f"{results['Profit Margin']:.2%}"
        )

        col4, col5, col6 = st.columns(3)

        col4.metric(
            "ROE",
            f"{results['ROE']:.2%}"
        )

        col5.metric(
            "ROA",
            f"{results['ROA']:.2%}"
        )

        col6.metric(
            "Debt / Equity",
            f"{results['Debt-to-Equity']:.2f}"
        )

        st.subheader("Liquidity")

        st.metric(
            "Current Ratio",
            f"{results['Current Ratio']:.2f}"
        )

        st.divider()

        st.subheader("Financial Trend")

        chart_data = edited_data.set_index("Year")

        st.line_chart(
            chart_data[
                ["Revenue", "Net Income"]
            ]
        )

        st.success(
            "Analysis complete. The results are based on the financial "
            "data entered above."
        )


# ==========================================
# OTHER MODULES
# ==========================================

else:

    st.header(option)

    st.info(
        "🚧 This module is currently under development."
    )
