def calculate_growth(current, previous):
    if previous == 0:
        return 0
    return (current / previous) - 1


def calculate_ratios(
    revenue,
    net_income,
    total_assets,
    shareholders_equity,
    total_debt,
    current_assets,
    current_liabilities
):
    ratios = {}

    ratios["Profit Margin"] = (
        net_income / revenue if revenue else 0
    )

    ratios["ROA"] = (
        net_income / total_assets if total_assets else 0
    )

    ratios["ROE"] = (
        net_income / shareholders_equity
        if shareholders_equity else 0
    )

    ratios["Debt-to-Equity"] = (
        total_debt / shareholders_equity
        if shareholders_equity else 0
    )

    ratios["Current Ratio"] = (
        current_assets / current_liabilities
        if current_liabilities else 0
    )

    return ratios


def analyze_company(data):
    """
    Analyze historical company financial data.
    """

    latest = data.iloc[-1]
    previous = data.iloc[-2]

    revenue_growth = calculate_growth(
        latest["Revenue"],
        previous["Revenue"]
    )

    earnings_growth = calculate_growth(
        latest["Net Income"],
        previous["Net Income"]
    )

    ratios = calculate_ratios(
        latest["Revenue"],
        latest["Net Income"],
        latest["Total Assets"],
        latest["Equity"],
        latest["Debt"],
        latest["Current Assets"],
        latest["Current Liabilities"]
    )

    return {
        "Revenue Growth": revenue_growth,
        "Earnings Growth": earnings_growth,
        **ratios
    }
