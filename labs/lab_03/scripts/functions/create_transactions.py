import json
from pathlib import Path


TRANSACTIONS_FILE = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "system"
    / "transactions"
    / "transactions.json"
)

TRANSACTIONS_FILE.parent.mkdir(parents=True, exist_ok=True)


def load_transactions():
    if TRANSACTIONS_FILE.exists():
        with open(TRANSACTIONS_FILE, "r") as f:
            return json.load(f)
    return []


def save_transactions(transactions):
    with open(TRANSACTIONS_FILE, "w") as f:
        json.dump(transactions, f, indent=4)


def get_transaction_type():
    valid_types = ["contribution", "withdrawal", "buy", "sell"]

    while True:
        t = input("Enter type (contribution, withdrawal, buy, sell): ").strip().lower()
        if t in valid_types:
            return t
        print("Invalid type.")


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number.")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid integer.")


def create_transaction(working_date, transactions):
    t_type = get_transaction_type()

    transaction = {
        "date": working_date,
        "type": t_type,
        "record_number": len(transactions) + 1,
    }

    if t_type in ["contribution", "withdrawal"]:
        transaction["ticker"] = "$$$$"
        transaction["shares"] = get_float("Enter amount: ")
        transaction["price"] = 1.0
    else:
        transaction["ticker"] = input("Enter ticker: ").strip().upper()
        transaction["shares"] = get_int("Enter shares: ")
        transaction["price"] = get_float("Enter price: ")

    return transaction


def enter_transactions():
    transactions = load_transactions()

    working_date = input("Enter working date (YYYY-MM-DD): ").strip()

    while True:
        transaction = create_transaction(working_date, transactions)
        transactions.append(transaction)

        # keep sorted by date then ticker
        transactions.sort(key=lambda t: (t["date"], t["ticker"]))
        save_transactions(transactions)

        print("Saved:", transaction)

        again = input("Another transaction for this date? (y/n): ").strip().lower()
        if again != "y":
            break


def main():
    enter_transactions()


if __name__ == "__main__":
    main()
