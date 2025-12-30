import requests
import json
from pathlib import Path

API_URL = "https://api.scryfall.com"

def download_bulk_cards(output_path="data/raw/cards.json"):

    print("Buscando metadados do bulk...")
    bulk_meta = requests.get( f"{API_URL}/bulk-data")
    bulk_meta.raise_for_status()

    bulk_data = bulk_meta.json()["data"]

    default_cards = next( b for b in bulk_data if b["type"] == "default_cards" ) 

    download_url = default_cards["download_uri"]
    print("Download iniciado... (isso pode demorar)")

    response = requests.get(download_url)
    response.raise_for_status()

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(response.json(), f)

    print(f"Bulk salvo em {output_path}")
