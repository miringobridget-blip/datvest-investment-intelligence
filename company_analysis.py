def calculate_ratios(
    revenue,
    net_income,
    total_assets,
    shareholders_equity,
    total_debt,
    current_assets,
    current_liabilities
):
    """
    Calculate key financial ratios.
    """

    ratios = {}

    # Profitability
    ratios["Profit Margin"] = net_income / revenue if revenue else 0

    ratios["ROA"] = net_income / total_assets if total_assets else 0

    ratios["ROE"] = (
        net_income / shareholders_equity
        if shareholders_equity
        else 0
    )

    # Leverage
    ratios["Debt-to-Equity"] = (
        total_debt / shareholders_equity
        if shareholders_equity
        else 0
    )

    # Liquidity
    ratios["Current Ratio"] = (
        current_assets / current_liabilities
        if current_liabilities
        else 0
    )

    return ratios
