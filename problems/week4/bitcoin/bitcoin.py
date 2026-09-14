import json
import requests
import sys


try:

    number = sys.argv[1]
    n = float(number)



    key = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=apikey")

    text = key.json()

    bitcoin_dict = text["data"]

    print(bitcoin_dict["priceUsd"])


except requests.RequestException:
    ...

except ValueError:
    sys.exit("Command-line argument is not a number")

except IndexError:
    sys.exit("Missing command-line argument")