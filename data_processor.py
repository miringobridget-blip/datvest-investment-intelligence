import pandas as pd


REQUIRED_COLUMNS = [
    "Year",
    "Revenue",
    "Net Income",
    "Total Assets",
    "Equity",
    "Debt",
    "Current Assets",
    "Current Liabilities"
]


def load_file(uploaded_file):

    file_name = uploaded_file.name.lower()

    if file_name.endswith(".csv"):

        data = pd.read_csv(uploaded_file)

    elif file_name.endswith(".xlsx"):

        data = pd.read_excel(uploaded_file)

    else:

        raise ValueError(
            "Unsupported file type. Please upload CSV or Excel."
        )

    return data


def validate_data(data):

    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in data.columns
    ]

    if missing_columns:

        return False, missing_columns

    return True, []


def clean_data(data):

    data = data.copy()

    data["Year"] = pd.to_numeric(
        data["Year"],
        errors="coerce"
    )

    numeric_columns = [
        "Revenue",
        "Net Income",
        "Total Assets",
        "Equity",
        "Debt",
        "Current Assets",
        "Current Liabilities"
    ]

    for column in numeric_columns:

        data[column] = pd.to_numeric(
            data[column],
            errors="coerce"
        )

    data = data.dropna(
        subset=["Year"]
    )

    data = data.sort_values(
        "Year"
    )

    return data
