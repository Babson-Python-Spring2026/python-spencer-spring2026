import json

prices_by_date = {}
prices_by_ticker = {}

# load splits keyed by date
with open('classes/04-06 M/my_data/system/splits_dates.json', 'r') as f:
    splits_by_date = json.load(f)

# load dividends keyed by date
with open('classes/04-06 M/my_data/system/dividends_dates.json', 'r') as f:
    dividends_by_date = json.load(f)

# read prices
with open('classes/04-06 M/my_data/source/portfolio_prices_raw_and_split_adjusted_20260331b.csv', 'r') as f:
    next(f)  # skip header

    for line in f:
        date, ticker, raw, adj = line.strip().split(',')

        # defaults: no split = 1:1, no dividend = 0.0
        shares_in = 1
        shares_out = 1
        dividend = 0.0

        # check for splits on this date
        if date in splits_by_date:
            for split_record in splits_by_date[date]:
                if split_record['ticker'] == ticker:
                    shares_in = split_record['shares_in']
                    shares_out = split_record['shares_out']
                    break

        # check for dividends on this date
        if date in dividends_by_date:
            for div_record in dividends_by_date[date]:
                if div_record['ticker'] == ticker:
                    dividend = float(div_record['dividend'])
                    break

        prices_by_date.setdefault(date, []).append({
            'ticker': ticker,
            'raw_price': float(raw),
            'shares_in': shares_in,
            'shares_out': shares_out,
            'dividend': dividend
        })

        prices_by_ticker.setdefault(ticker, []).append({
            'date': date,
            'raw_price': float(raw),
            'shares_in': shares_in,
            'shares_out': shares_out,
            'dividend': dividend
        })

with open('classes/04-06 M/my_data/system/prices_dates.json', 'w') as f:
    json.dump(prices_by_date, f, indent=2)

with open('classes/04-06 M/my_data/system/prices_tickers.json', 'w') as f:
    json.dump(prices_by_ticker, f, indent=2)
