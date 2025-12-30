from extract import get_cards_by_set

cards = get_cards_by_set("khm")

print(f'cartas extraídas: {len(cards)}')
print(cards[300]["name"])
