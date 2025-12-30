from extract import download_bulk_cards
from transform import transform_cards

# if __name__ == "__main__":
#     download_bulk_cards()


if __name__ == "__main__":
    count = 0

    for card in transform_cards():
        if count < 5:
            print(card)
        count += 1

    print("Total processado:", count)