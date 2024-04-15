import requests
import webbrowser


def make_request(url):
    try:
        response = requests.get(url)
        return response
    except requests.exceptions.ConnectionError:
        pass


target_input = "google.com"

with open("subdomainlist.txt", "r") as alp:
    for word in alp:
        word = word.strip()
        url = "http://" + word + "." + target_input
        response = make_request(url)
        if response:  # "response none değilse" demek
            print("Found subdomain ---> " + url)
# Not: strip kullanımı
# txt = ",,,,,rrttgg.....banana....rrr"
# x = txt.strip(",.grt")
# print(x)
