import requests
import time

BASE_URL = "https://api.scryfall.com/cards/search"
API_URL = "https://api.scryfall.com"

def get_cards_by_set(set_code, max_pages=None):
    cards = []
    params = {"q" : f"set:{set_code}"}
    url = BASE_URL
    page = 1
    has_more = True

    while has_more:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        cards.extend(data["data"])

        print(f"página {page} | total de cartas: {len(cards)} ")

        has_more = data.get("has_more", False)
        if has_more:
            url = data["next_page"]
            params = None
        page += 1

        if max_pages and page > max_pages:
            break

        time.sleep(0.1)
    
    return cards
