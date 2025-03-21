import requests

def get_binance_listings():
    url = "https://api.binance.com/api/v3/exchangeInfo"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return [coin['symbol'] for coin in data['symbols']]
    return []

if __name__ == "__main__":
    listings = get_binance_listings()
    print("Binance New Listings:", listings)
