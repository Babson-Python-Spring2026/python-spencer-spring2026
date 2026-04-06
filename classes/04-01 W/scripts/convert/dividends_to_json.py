import json

# two dictionaries - one keyed by date, one keyed by ticker
dividends_by_date = {}
dividends_by_ticker = {}

with open('classes/04-01 W/data/source/portfolio_dividends_20260331b.csv', 'r') as f:
    
    next(f)  # skip header

    for line in f:
        tokens = line.strip().split(',')

        date = tokens[0]
        ticker = tokens[1]
        dividend = tokens[2]

        # by date: date -> list of {ticker, dividend}
        if date not in dividends_by_date:
            dividends_by_date[date] = []

        dividends_by_date[date].append({
            'ticker': ticker,
            'dividend': dividend
        })

        # by ticker: ticker -> list of {date, dividend}
        if ticker not in dividends_by_ticker:
            dividends_by_ticker[ticker] = []

        dividends_by_ticker[ticker].append({
            'date': date,
            'dividend': dividend
        })


with open('classes/04-01 W/data/system/dividends_dates.json', 'w') as f:
    json.dump(dividends_by_date, f, indent=2)

with open('classes/04-01 W/data/system/dividends_tickers.json', 'w') as f:
    json.dump(dividends_by_ticker, f, indent=2)
