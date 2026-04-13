import json
from pathlib import Path

from create_cash_by_date import build_cash_by_date


BASE_FOLDER = Path(__file__).resolve().parents[2] / "data" / "system"

MKT_DATES_FILE = BASE_FOLDER / "mkt_dates.json"
CASH_FILE = BASE_FOLDER / "positions_by_date" / "cash_by_date.json"


def load_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


def get_valid_date(mkt_dates):
    while True:
        date = input("Enter date (YYYY-MM-DD): ").strip()
        if date in mkt_dates:
            return date
        print("Invalid date. Please enter a valid market date.")


def get_cash_by_date():
    mkt_dates = load_json(MKT_DATES_FILE)
    date = get_valid_date(mkt_dates)

    # rebuild fresh from transactions
    build_cash_by_date()

    cash_by_date = load_json(CASH_FILE)
    cash = cash_by_date[date]

    print(f"\nDate: {date}")
    print(f"Cash: ${cash:,.2f}")


if __name__ == "__main__":
    get_cash_by_date()
