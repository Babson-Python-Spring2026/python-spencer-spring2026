import json

dividends_by_date = {}
dividends_by_ticker = {}

with open('classes/04-06 M/my_data/source/portfolio_dividends_20260331b.csv', 'r') as f:

    next(f)  # skip header line

    for line in f:
        date, ticker, dividend = line.strip().split(',')

        dividends_by_date.setdefault(date, []).append({
            'ticker': ticker,
            'dividend': dividend
        })

        dividends_by_ticker.setdefault(ticker, []).append({
            'date': date,
            'dividend': dividend
        })

with open('classes/04-06 M/my_data/system/dividends_dates.json', 'w') as f:
    json.dump(dividends_by_date, f, indent=2)

with open('classes/04-06 M/my_data/system/dividends_tickers.json', 'w') as f:
    json.dump(dividends_by_ticker, f, indent=2)
