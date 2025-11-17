from collections import namedtuple

Honkai_Karakter = namedtuple('Honkai_Karakter', ['nama', 'planet', 'pekerjaan'])

anaxa = Honkai_Karakter('Anaxa', 'Amphoreus', 'Professor')

print(f"{anaxa[0]} adalah seorang {anaxa.pekerjaan} di planet {getattr(anaxa, "planet")}")