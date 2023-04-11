"""
Funkce filtruje prvky ze seznamu (např. zprávy v TV nebo na obrazovce)
podle následujících pravidel:
        1. Odstraní dlouhý a krátký text (to, co není 3-50 znaků dlouhé)
        2. Smaže čísla, která nejsou celá
        3. Odstraní duplicity (nechá jen jeden prvek)
        4. Odstraní slova, která jsou v seznamu (negativní slova)
        5. Odstraní některé odkazy na webové stránky
"""


import re

def algo(zpravy, min, max, negativni):

    filtrovane = []
    filtrovane = [x for x in zpravy if isinstance(x, int) or (isinstance(x, str) and min <= len(x) <= max)]
    filtrovane = [x for x in filtrovane if not isinstance(x, float) or x.is_integer()]
    filtrovane = list(set(filtrovane))
    filtrovane = [x for x in filtrovane if not any(y.lower() in str(x).lower() for y in negativni)]
    url_format = r"(?:https?://)?(?:www\.)?([a-z0-9]+(?:-[a-z0-9]+)*\.(?:com|org|net|gov|edu|biz|info|io|uk|us|ca||cn|to|au|nz|in|co|eu|cz|be))"
    filtrovane = [x for x in filtrovane if not re.match(url_format, str(x))]

    print(filtrovane)
    return filtrovane



min = 3
max = 50
zpravy = [123,
         123,
         728003796.6,
         728003796.0,
         728003796,
         'www.reklama.com',
         'reklama.co.uk,'
         'špatný',
         'Ten herec je fakt dobrý!',
         'Nejlepší písnička.',
         'best',
         'Špatný song',
         'špatný song',
         '1/10',
         '10/10',
         'Ty výkony !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!',
         'Kdybych měl možnost...']

negativni = ["špatný",
            "nevýhodný",
            "nepříjemný",
            "nechutný",
            "neuspokojivý",
            "nezajímavý",
            "nevhodný",
            "nekvalitní",
            "neefektivní",
            "nebezpečný",
            "nedostatečný",
            "neuspěšný",
            "neúspěšný",
            "nedobrý",
            "nechvalný",
            "(dot)",
            "dot"]


algo(zpravy, min, max, negativni)
