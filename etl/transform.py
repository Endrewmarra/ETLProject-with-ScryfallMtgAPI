import ijson

def read_cards_stream(path="data/raw/cards.json"):
    with open(path, "rb") as f:
        for card in ijson.items(f, "item"):
            yield card


def normalize_card(card):
    return {
        "_id": card.get("id"),
        "name": card.get("name"),
        "set": card.get("set"),
        "set_name": card.get("set_name"),
        "colors": card.get("colors", []),
        "type_line": card.get("type_line"),
        "cmc": str(card.get("cmc")),
        "rarity": card.get("rarity"),
    }



def extract_main_type(type_line):
    if not type_line:
        return "Unknown"
    return type_line.split("—")[0].strip()


def transform_cards():
    for card in read_cards_stream():
        normalized = normalize_card(card)
        normalized["main_type"] = extract_main_type(
            normalized["type_line"]
        )
        yield normalized
