from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError


def get_collection(
    db_name="mtg",
    collection_name="cards"
):
    
    client = MongoClient("mongodb://localhost:27017")
    db = client[db_name]
    collection = db[collection_name]
    return collection


def load_cards(cards_generator):
    
    collection = get_collection()

    inserted = 0
    skipped = 0

    for card in cards_generator:
        try:
            collection.insert_one(card)
            inserted += 1
        except DuplicateKeyError:
            skipped += 1

        total = inserted + skipped
        if total % 1000 == 0:
            print(
                f"Processadas: {total} | "
                f"Inseridas: {inserted} | "
                f"Ignoradas: {skipped}"
            )

    print("LOAD FINALIZADO")
    print(f"Inseridas: {inserted}")
    print(f"Ignoradas: {skipped}")
