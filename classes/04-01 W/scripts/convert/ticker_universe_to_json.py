import json

# pull unique tickers from the prices file
tickers = set()

with open('classes/04-01 W/data/source/portfolio_prices_raw_and_split_adjusted_20260331b.csv', 'r') as f:
    next(f)  # skip header
    for line in f:
        tokens = line.strip().split(',')
        tickers.add(tokens[1])

# sort alphabetically
ticker_universe = sorted(list(tickers))

with open('classes/04-01 W/data/system/ticker_universe.json', 'w') as f:
    json.dump(ticker_universe, f, indent=2)
