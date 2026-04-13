import json
from pathlib import Path


BASE_FOLDER = Path(__file__).resolve().parents[2] / "data" / "system"

TRANSACTIONS_FILE = BASE_FOLDER / "transactions" / "transactions.json"
POSITIONS_FILE = BASE_FOLDER / "positions_by_date" / "stocks_by_date.json"
PRICES_DATES_FILE = BASE_FOLDER / "prices_dates.json"
MKT_DATES_FILE = BASE_FOLDER / "mkt_dates.json"

CASH_FILE = BASE_FOLDER / "positions_by_date" / "cash_by_date.json"
CASH_FILE.parent.mkdir(parents=True, exist_ok=True)


def load_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


def group_transactions_by_date(transactions):
    by_date = {}
    for t in transactions:
        d = t["date"]
        if d not in by_date:
            by_date[d] = []
        by_date[d].append(t)
    return by_date


def build_cash_by_date():
    transactions = load_json(TRANSACTIONS_FILE)
    positions_by_date = load_json(POSITIONS_FILE)
    prices_by_date = load_json(PRICES_DATES_FILE)
    mkt_dates = load_json(MKT_DATES_FILE)

    transactions_by_date = group_transactions_by_date(transactions)

    cash = 0.0
    cash_by_date = {}

    for date in mkt_dates:

        # 1. apply transaction cash flows
        if date in transactions_by_date:
            for t in transactions_by_date[date]:
                t_type = t["type"]
                shares = t["shares"]
                price = t["price"]

                if t_type == "contribution":
                    cash += shares
                elif t_type == "withdrawal":
                    cash -= shares
                elif t_type == "buy":
                    cash -= shares * price
                elif t_type == "sell":
                    cash += shares * price

        # 2. apply dividends based on current stock positions
        if date in prices_by_date:
            pos_lookup = {
                p["ticker"]: p["shares"]
                for p in positions_by_date[date]
            }

            for record in prices_by_date[date]:
                dividend = record["dividend"]
                ticker = record["ticker"]

                if dividend != 0.0 and ticker in pos_lookup:
                    cash += pos_lookup[ticker] * dividend

        # 3. store result
        cash_by_date[date] = round(cash, 2)

    # save
    with open(CASH_FILE, "w") as f:
        json.dump(cash_by_date, f, indent=4)

    print(f"Created: {CASH_FILE}")


def main():
    build_cash_by_date()


if __name__ == "__main__":
    main()
