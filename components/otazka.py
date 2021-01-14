from components.open import zemepis_json, dejepis_json, literatura_json


def blit_otazky(i, okruh):
    if okruh == 0:
        return zemepis_json['otazky'][i - 1]['otazka']
    elif okruh == 1:
        return dejepis_json['otazky'][i - 1]['otazka']
    elif okruh == 2:
        return literatura_json['otazky'][i - 1]['otazka']


def blit_odpoved(i, num, okruh):
    if okruh == 0:
        return zemepis_json['otazky'][i - 1][f'odpoved{num}']
    elif okruh == 1:
        return dejepis_json['otazky'][i - 1][f'odpoved{num}']
    elif okruh == 2:
        return literatura_json['otazky'][i - 1][f'odpoved{num}']
