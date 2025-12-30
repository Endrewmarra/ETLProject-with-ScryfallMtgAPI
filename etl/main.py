import requests
from extract import get_sets

sets = get_sets()

print(f'Total de coleções: {len(sets)}')
