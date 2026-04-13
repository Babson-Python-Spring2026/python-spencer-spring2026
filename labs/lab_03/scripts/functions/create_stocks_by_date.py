import json
from pathlib import Path


BASE_FOLDER = Path(__file__).resolve().parents[2] / "data" / "system"

TRANSACTIONS_FILE = BASE_FOLDER / "transactions" / "transactions.json"
PRICES_DATES_FILE = BASE_FOLDER / "prices_dates.json"
MKT_DATES_FILE = BASE_FOLDER / "mkt_dates.json"
STOCKS_BY_DATE_FILE = BASE_FOLDER / "positions_by_date" / "stocks_by_date.json"

STOCKS_BY_DATE_FILE.parent.mkdir(parents=True, exist_ok=True)


# -------------------------------------------------------
# LOAD
# -------------------------------------------------------

def load_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


# -------------------------------------------------------
# SPLITS
# -------------------------------------------------------

def build_split_lookup(prices_by_date):
    """Go through prices_dates.json and find any date where
    shares_in != shares_out. That means a split happened."""
    split_lookup = {}

    for date, records in prices_by_date.items():
        split_lookup[date] = {}

        for record in records:
            if record["shares_in"] != record["shares_out"]:
                split_lookup[date][record["ticker"]] = {
                    "shares_in": record["shares_in"],
                    "shares_out": record["shares_out"],
                }

    return split_lookup


def apply_split(position, split_record):
    """Adjust shares and avg cost for a stock split."""
    shares_in = split_record["shares_in"]
    shares_out = split_record["shares_out"]

    position["shares"] = (position["shares"] / shares_in) * shares_out
    position["average_cost"] = (position["average_cost"] / shares_out) * shares_in

    if position["shares"] == 0:
        position["average_cost"] = 0.0


# -------------------------------------------------------
# TRANSACTIONS
# -------------------------------------------------------

def group_transactions_by_date(transactions):
    transactions.sort(key=lambda t: (t["date"], t["record_number"]))

    by_date = {}
    for t in transactions:
        date = t["date"]
        if date not in by_date:
            by_date[date] = []
        by_date[date].append(t)

    return by_date


def apply_transaction(position, transaction):
    """Update a single stock position based on a buy or sell."""
    t_type = transaction["type"]
    shares = transaction["shares"]
    price = transaction["price"]

    cur_shares = position["shares"]
    cur_avg = position["average_cost"]

    if t_type == "buy":
        if cur_shares == 0:
            position["shares"] = shares
            position["average_cost"] = price

        elif cur_shares > 0:
            new_shares = cur_shares + shares
            new_avg = ((cur_shares * cur_avg) + (shares * price)) / new_shares
            position["shares"] = new_shares
            position["average_cost"] = new_avg

        else:
            # covering a short
            if shares < abs(cur_shares):
                position["shares"] = cur_shares + shares
            elif shares == abs(cur_shares):
                position["shares"] = 0
                position["average_cost"] = 0.0
            else:
                remaining = shares - abs(cur_shares)
                position["shares"] = remaining
                position["average_cost"] = price

    elif t_type == "sell":
        if cur_shares == 0:
            position["shares"] = -shares
            position["average_cost"] = price

        elif cur_shares < 0:
            # increasing short
            new_shares = cur_shares - shares
            new_avg = ((abs(cur_shares) * cur_avg) + (shares * price)) / abs(new_shares)
            position["shares"] = new_shares
            position["average_cost"] = new_avg

        else:
            # reducing long
            if shares < cur_shares:
                position["shares"] = cur_shares - shares
            elif shares == cur_shares:
                position["shares"] = 0
                position["average_cost"] = 0.0
            else:
                remaining = shares - cur_shares
                position["shares"] = -remaining
                position["average_cost"] = price


# -------------------------------------------------------
# SNAPSHOT
# -------------------------------------------------------

def make_snapshot(positions):
    snapshot = []
    for ticker in sorted(positions):
        snapshot.append({
            "ticker": positions[ticker]["ticker"],
            "shares": positions[ticker]["shares"],
            "average_cost": round(positions[ticker]["average_cost"], 6),
        })
    return snapshot


# -------------------------------------------------------
# MAIN BUILD
# -------------------------------------------------------

def build_stocks_by_date():
    transactions = load_json(TRANSACTIONS_FILE)
    prices_by_date = load_json(PRICES_DATES_FILE)
    mkt_dates = load_json(MKT_DATES_FILE)

    split_lookup = build_split_lookup(prices_by_date)
    transactions_by_date = group_transactions_by_date(transactions)

    stocks = {}
    positions_by_date = {}

    for date in mkt_dates:
        # 1. apply splits for this date
        if date in split_lookup:
            for ticker, split_record in split_lookup[date].items():
                if ticker in stocks:
                    apply_split(stocks[ticker], split_record)

        # 2. apply buy/sell transactions for this date
        if date in transactions_by_date:
            for transaction in transactions_by_date[date]:
                if transaction["type"] not in ["buy", "sell"]:
                    continue

                ticker = transaction["ticker"]

                if ticker not in stocks:
                    stocks[ticker] = {
                        "ticker": ticker,
                        "shares": 0,
                        "average_cost": 0.0,
                    }

                apply_transaction(stocks[ticker], transaction)

        # 3. snapshot for this date
        positions_by_date[date] = make_snapshot(stocks)

    return positions_by_date


def save_positions(positions_by_date):
    with open(STOCKS_BY_DATE_FILE, "w") as f:
        json.dump(positions_by_date, f, indent=4)


def main():
    positions = build_stocks_by_date()
    save_positions(positions)
    print(f"Created: {STOCKS_BY_DATE_FILE}")


if __name__ == "__main__":
    main()
