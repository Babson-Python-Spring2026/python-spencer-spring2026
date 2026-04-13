import json
from pathlib import Path

from create_cash_by_date import build_cash_by_date
from create_stocks_by_date import build_stocks_by_date


# -------------------------------------------------------
# PATHS
# -------------------------------------------------------

BASE_FOLDER = Path(__file__).resolve().parents[2] / "data" / "system"

MKT_DATES_FILE = BASE_FOLDER / "mkt_dates.json"
PRICES_DATES_FILE = BASE_FOLDER / "prices_dates.json"
STOCKS_BY_DATE_FILE = BASE_FOLDER / "positions_by_date" / "stocks_by_date.json"
CASH_BY_DATE_FILE = BASE_FOLDER / "positions_by_date" / "cash_by_date.json"
PORTFOLIO_FOLDER = BASE_FOLDER / "positions_by_date"

PORTFOLIO_FOLDER.mkdir(parents=True, exist_ok=True)


# -------------------------------------------------------
# LOAD
# -------------------------------------------------------

def load_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


# -------------------------------------------------------
# INPUT
# -------------------------------------------------------

def get_valid_date(valid_dates):
    while True:
        date = input("Enter date (YYYY-MM-DD): ").strip()
        if date in valid_dates:
            return date
        print("Invalid date. Please enter a valid market date.")


# -------------------------------------------------------
# PRICE LOOKUP
# -------------------------------------------------------

def build_price_lookup(prices_by_date, date):
    lookup = {}
    for record in prices_by_date[date]:
        lookup[record["ticker"]] = record["raw_price"]
    return lookup


# -------------------------------------------------------
# BUILD PORTFOLIO
# -------------------------------------------------------

def build_portfolio_for_date(date):
    # rebuild from source every time
    build_stocks_by_date()
    build_cash_by_date()

    prices_by_date = load_json(PRICES_DATES_FILE)
    stocks_by_date = load_json(STOCKS_BY_DATE_FILE)
    cash_by_date = load_json(CASH_BY_DATE_FILE)

    price_lookup = build_price_lookup(prices_by_date, date)

    portfolio = []

    # stock rows
    for position in stocks_by_date[date]:
        ticker = position["ticker"]
        shares = int(position["shares"])
        avg_cost = float(position["average_cost"])
        mkt_price = float(price_lookup[ticker])

        portfolio.append({
            "ticker": ticker,
            "shares": shares,
            "average_cost": round(avg_cost, 2),
            "mkt_price": round(mkt_price, 2),
            "total_avg_cost": round(avg_cost * shares, 2),
            "total_mkt_value": round(mkt_price * shares, 2),
        })

    # cash row
    cash = float(cash_by_date[date])
    portfolio.append({
        "ticker": "$$$$",
        "shares": round(cash, 2),
        "average_cost": 1.00,
        "mkt_price": 1.00,
        "total_avg_cost": round(cash, 2),
        "total_mkt_value": round(cash, 2),
    })

    portfolio.sort(key=lambda p: p["ticker"])
    return portfolio


# -------------------------------------------------------
# DISPLAY
# -------------------------------------------------------

def print_header():
    header = (
        f"{'TICKER':<8} "
        f"{'SHARES':>15} "
        f"{'AVG_COST':>15} "
        f"{'MKT_PRICE':>15} "
        f"{'TOTAL_COST':>18} "
        f"{'TOTAL_MKT_VAL':>18}"
    )
    print(header)
    print("-" * len(header))


def print_portfolio(date, portfolio):
    print()
    print(f"Portfolio for {date}")
    print()
    print_header()

    for i, p in enumerate(portfolio, start=1):
        if p["ticker"] == "$$$$":
            shares_str = f"{p['shares']:,.2f}"
        else:
            shares_str = f"{int(p['shares']):,}"

        print(
            f"{p['ticker']:<8} "
            f"{shares_str:>15} "
            f"{p['average_cost']:>15,.2f} "
            f"{p['mkt_price']:>15,.2f} "
            f"{p['total_avg_cost']:>18,.2f} "
            f"{p['total_mkt_value']:>18,.2f}"
        )

        if i % 15 == 0 and i < len(portfolio):
            input("\nPress Return to continue...")
            print()
            print_header()
        elif i % 5 == 0 and i < len(portfolio):
            print()

    print()


# -------------------------------------------------------
# SAVE
# -------------------------------------------------------

def save_portfolio(date, portfolio):
    output_file = PORTFOLIO_FOLDER / f"portfolio_{date}.json"
    with open(output_file, "w") as f:
        json.dump(portfolio, f, indent=4)
    return output_file


# -------------------------------------------------------
# MAIN
# -------------------------------------------------------

def main():
    valid_dates = load_json(MKT_DATES_FILE)
    date = get_valid_date(valid_dates)

    portfolio = build_portfolio_for_date(date)
    output_file = save_portfolio(date, portfolio)
    print_portfolio(date, portfolio)

    print(f"Created: {output_file}")


if __name__ == "__main__":
    main()
