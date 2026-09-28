import streamlit as st
import pandas as pd

from company_analysis import analyze_company
from data_processor import load_file, validate_data, clean_data


st.set_page_config(
    page_title="Datvest Investment Intelligence",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Datvest Investment Intelligence")
st.caption("Financial analysis and investment research platform")

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


if option == "Dashboard":

    st.header("Investment Intelligence Dashboard")

    st.write(
        """
        Welcome to the investment research platform.

        This system is being developed to support:
        financial analysis, risk assessment, valuation,
        portfolio analysis and investment research.
        """
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    col1.metric("Modules", "6")
    col2.metric("Status", "Development")
    col3.metric("Data Engine", "Active")

    st.info("Select Company Analysis from the sidebar.")


elif option == "Company Analysis":

    st.header("🏢 Company Analysis")

    st.write(
        "Upload historical financial data for the company you want to analyze."
    )

    company_name = st.text_input(
        "Company Name",
        placeholder="e.g. Delta Corporation"
    )

    st.subheader("📁 Upload Financial Data")

    uploaded_file = st.file_uploader(
        "Upload CSV or Excel financial data",
        type=["csv", "xlsx"]
    )

    st.divider()

    st.subheader("Required Data Format")

    required_columns = [
        "Year",
        "Revenue",
        "Net Income",
        "Total Assets",
        "Equity",
        "Debt",
        "Current Assets",
        "Current Liabilities"
    ]

    st.code(", ".join(required_columns))

    if uploaded_file is not None:

        st.success(
            f"File uploaded: {uploaded_file.name}"
        )

        try:

            data = load_file(uploaded_file)

            st.subheader("🔍 Uploaded Data")

            st.dataframe(
                data,
                width="stretch"
            )

            valid, missing_columns = validate_data(data)

            if not valid:

                st.error("The uploaded file is missing required columns.")

                st.write("Missing columns:")

                for column in missing_columns:
                    st.write(f"❌ {column}")

            else:

                st.success("✓ Data structure validated successfully.")

                data = clean_data(data)

                st.subheader("📊 Cleaned Financial Data")

                st.dataframe(
                    data,
                    width="stretch"
                )

                if len(data) < 2:

                    st.warning(
                        "At least two years of data are required."
                    )

                else:

                    if st.button(
                        "🚀 Analyze Company",
                        type="primary"
                    ):

                        results = analyze_company(data)

                        st.divider()

                        st.subheader(
                            f"📈 {company_name or 'Company'} Financial Analysis"
                        )

                        st.subheader("Growth")

                        col1, col2 = st.columns(2)

                        col1.metric(
                            "Revenue Growth",
                            f"{results['Revenue Growth']:.2%}"
                        )

                        col2.metric(
                            "Earnings Growth",
                            f"{results['Earnings Growth']:.2%}"
                        )

                        st.subheader("Profitability")

                        col1, col2, col3 = st.columns(3)

                        col1.metric(
                            "Profit Margin",
                            f"{results['Profit Margin']:.2%}"
                        )

                        col2.metric(
                            "ROE",
                            f"{results['ROE']:.2%}"
                        )

                        col3.metric(
                            "ROA",
                            f"{results['ROA']:.2%}"
                        )

                        st.subheader("Leverage & Liquidity")

                        col1, col2 = st.columns(2)

                        col1.metric(
                            "Debt / Equity",
                            f"{results['Debt-to-Equity']:.2f}"
                        )

                        col2.metric(
                            "Current Ratio",
                            f"{results['Current Ratio']:.2f}"
                        )

                        st.subheader("Financial Trend")

                        chart_data = data.set_index("Year")

                        st.line_chart(
                            chart_data[
                                ["Revenue", "Net Income"]
                            ]
                        )

                        st.success(
                            "Analysis completed using the uploaded financial data."
                        )

        except Exception as error:

            st.error(
                "The system could not process the uploaded file."
            )

            st.write(f"Error: {error}")


else:

    st.header(option)

    st.info(
        "🚧 This module is currently under development."
    )
