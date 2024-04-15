import time
import requests


def get_crypto_currency():
    response = requests.get("https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json")
    print(response)
    if response.status_code == 200:
        print("Success...")
        time.sleep(1)
        return response.json()


crypto_response = get_crypto_currency()
user_input = input("Enter your currency: ")
for crypto in crypto_response:
    if crypto["currency"] == user_input:
        print(crypto["price"])
        break
