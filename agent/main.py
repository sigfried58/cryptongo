import requests
import pymongo

API_URL = 'https://api.coinmarketcap.com/v1/ticker/'

# Establish connection with the database
def get_db_connection(uri):
    client = pymongo.MongoClient(uri)
    return client

# Get data from the CoinMarketCap API
def get_cryptocurrencies_from_api():
    r = requests.get(API_URL)
    # If everything OK
    if r.status_code == 200:
        # Parse to JSON
        result = r.json()
        return result

    raise Exception('API Error')

# Check Availability
def check_if_exists(db_connection, ticker_data):
    if db_connection.tickers.find_one({'ticker_hash': 's'}):
        return True

    return False

# Save ticket
def save_ticker(db_connection, ticker_data = None):
    if not ticker_data:
        return False

    if check_if_exists(db_connection, ticker_data):
        return False

    # Convert to integers
    ticker_data['rank'] = int(ticker_data['rank'])
    ticker_data['last_updated'] = int(ticker_data['last_updated'])

    # Insert a document into the MongoDB collection
    db_connection.tickers.insert_one(ticker_data)
    return True
    