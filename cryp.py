import requests
from tabulate import tabulate

def fetch_crypto_prices():
    cryptos = 'bitcoin,ethereum,binancecoin,ripple,solana,cardano,polkadot,avalanche-2'
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={cryptos}&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    return data

def display_in_table(data):
    table_data = []
    for crypto, value in data.items():
        table_data.append([crypto.capitalize(), value['usd']])

    headers = ["Cryptocurrency", "Price (USD)"]
    print(tabulate(table_data, headers, tablefmt="grid"))

if __name__ == "__main__":
    prices = fetch_crypto_prices()
    display_in_table(prices)
