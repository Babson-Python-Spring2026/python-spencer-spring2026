from fractions import Fraction
import json

# first load splits into a lookup: (date, ticker) -> (shares_in, shares_out)
splits_lookup = {}
with open('classes/04-01 W/data/source/portfolio_splits_true_splits_only_20260331b.csv', 'r') as f:
    next(f)  # skip header
    for line in f:
        tokens = line.strip().split(',')
        date = tokens[0]
        ticker = tokens[1]
        split_factor = Fraction(tokens[2])
        splits_lookup[(date, ticker)] = (split_factor.denominator, split_factor.numerator)

# load dividends into a lookup: (date, ticker) -> dividend amount
dividends_lookup = {}
with open('classes/04-01 W/data/source/portfolio_dividends_20260331b.csv', 'r') as f:
    next(f)  # skip header
    for line in f:
        tokens = line.strip().split(',')
        date = tokens[0]
        ticker = tokens[1]
        dividend = float(tokens[2])
        dividends_lookup[(date, ticker)] = dividend

# now read prices and build both dictionaries
prices_by_date = {}
prices_by_ticker = {}

with open('classes/04-01 W/data/source/portfolio_prices_raw_and_split_adjusted_20260331b.csv', 'r') as f:
    next(f)  # skip header

    for line in f:
        tokens = line.strip().split(',')
        date = tokens[0]
        ticker = tokens[1]
        raw_price = float(tokens[2])

        # look up split info for this date+ticker, default to 1:1
        shares_in, shares_out = splits_lookup.get((date, ticker), (1, 1))

        # look up dividend for this date+ticker, default to 0.0
        dividend = dividends_lookup.get((date, ticker), 0.0)

        # by date
        if date not in prices_by_date:
            prices_by_date[date] = []

        prices_by_date[date].append({
            'ticker': ticker,
            'raw_price': raw_price,
            'shares_in': shares_in,
            'shares_out': shares_out,
            'dividend': dividend
        })

        # by ticker
        if ticker not in prices_by_ticker:
            prices_by_ticker[ticker] = []

        prices_by_ticker[ticker].append({
            'date': date,
            'raw_price': raw_price,
            'shares_in': shares_in,
            'shares_out': shares_out,
            'dividend': dividend
        })


with open('classes/04-01 W/data/system/prices_dates.json', 'w') as f:
    json.dump(prices_by_date, f, indent=2)

with open('classes/04-01 W/data/system/prices_tickers.json', 'w') as f:
    json.dump(prices_by_ticker, f, indent=2)
