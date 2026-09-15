import json
import requests
import sys


try:

    number = sys.argv[1]
    n = float(number)

    key = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=your_key")

    text = key.json()

    bitcoin_dict = text["data"]
    bitcoin = bitcoin_dict["priceUsd"]
    bitcoin = float(bitcoin)

    amount = bitcoin * n
    print(f"${amount:,.4f}")


except requests.RequestException:
    ...

except ValueError:
    sys.exit("Command-line argument is not a number")

except IndexError:
    sys.exit("Missing command-line argument")