from extract import download_bulk_cards
from transform import transform_cards
from load import load_cards

def main():
    download_bulk_cards()
    cards = transform_cards()
    load_cards(cards)

if __name__ == "__main__":
    main()