import json
from pathlib import Path


BASE_FOLDER = Path(__file__).resolve().parents[2] / "data" / "system"

TRANSACTIONS_FILE = BASE_FOLDER / "transactions" / "transactions.json"
TICKER_UNIVERSE_FILE = BASE_FOLDER / "ticker_universe.json"


def load_json(file_path):
    if file_path.exists():
        with open(file_path, "r") as f:
            return json.load(f)
    return []


def get_valid_ticker(valid_tickers):
    while True:
        ticker = input("Enter ticker: ").strip().upper()
        if ticker in valid_tickers:
            return ticker
        print("Invalid ticker.")


def print_header():
    header = (
        f"{'DATE':<12} "
        f"{'TYPE':<14} "
        f"{'TICKER':<8} "
        f"{'SHARES':>12} "
        f"{'PRICE':>12} "
        f"{'RECORD':>8}"
    )
    print(header)
    print("-" * len(header))


def list_transactions_for_ticker():
    transactions = load_json(TRANSACTIONS_FILE)
    valid_tickers = load_json(TICKER_UNIVERSE_FILE)

    ticker = get_valid_ticker(valid_tickers)

    # filter to just this ticker
    matching = [t for t in transactions if t["ticker"] == ticker]
    matching.sort(key=lambda t: t["date"])

    print()

    if len(matching) == 0:
        print(f"No transactions found for {ticker}.")
        return

    print_header()

    for i, t in enumerate(matching, start=1):
        if t["ticker"] == "$$$$":
            shares_str = f"{t['shares']:>12,.2f}"
        else:
            shares_str = f"{int(t['shares']):>12,}"

        print(
            f"{t['date']:<12} "
            f"{t['type']:<14} "
            f"{t['ticker']:<8} "
            f"{shares_str} "
            f"{t['price']:>12.2f} "
            f"{t['record_number']:>8}"
        )

        if i % 15 == 0 and i < len(matching):
            input("\nPress Return to continue...")
            print()
            print_header()
        elif i % 5 == 0 and i < len(matching):
            print()


def main():
    list_transactions_for_ticker()


if __name__ == "__main__":
    main()
