from components.open import zemepis_json
import random


def blit_otazky(i):
    print(zemepis_json['otazky'][i - 1]['otazka'])
    return zemepis_json['otazky'][i - 1]['otazka']


def blit_odpoved(i, num):
    print(zemepis_json['otazky'][i - 1][f'odpoved{num}'])
    return zemepis_json['otazky'][i - 1][f'odpoved{num}']
