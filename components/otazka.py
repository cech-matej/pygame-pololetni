from components.open import zemepis_json, dejepis_json, literatura_json
import random


def blit_otazky(i, okruh):
    if okruh == 0:
        print(zemepis_json['otazky'][i - 1]['otazka'])
        return zemepis_json['otazky'][i - 1]['otazka']
    elif okruh == 1:
        print(dejepis_json['otazky'][i - 1]['otazka'])
        return dejepis_json['otazky'][i - 1]['otazka']
    elif okruh == 2:
        print(literatura_json['otazky'][i - 1]['otazka'])
        return literatura_json['otazky'][i - 1]['otazka']


def blit_odpoved(i, num, okruh):
    if okruh == 0:
        print(zemepis_json['otazky'][i - 1][f'odpoved{num}'])
        return zemepis_json['otazky'][i - 1][f'odpoved{num}']
    elif okruh == 1:
        print(dejepis_json['otazky'][i - 1][f'odpoved{num}'])
        return dejepis_json['otazky'][i - 1][f'odpoved{num}']
    elif okruh == 2:
        print(literatura_json['otazky'][i - 1][f'odpoved{num}'])
        return literatura_json['otazky'][i - 1][f'odpoved{num}']
