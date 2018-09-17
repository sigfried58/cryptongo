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