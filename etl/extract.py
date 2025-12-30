import requests

def get_sets():
    url = "https://api.scryfall.com/sets"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["data"]