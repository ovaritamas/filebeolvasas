programnyelvek = []
with open('adatok\Timeline_of_ programming_languages.csv', 'r', encoding='utf-8') as forrasfajl:
    for i in range(2):
        next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        programnyelv = {"year": int(adatok[0]), "programming language": adatok[1], "first name":(adatok[2]), "last name of chief developer":(adatok[3])}
        programnyelvek.append(programnyelv)

print(programnyelvek)

for programnyelv in programnyelvek:
    print(f"{programnyelv["year"]} - {programnyelv["programming language"]} - {programnyelv["first name"]} - {programnyelv["last name of chief developer"]}")

"""Legfiatalabb nyelv"""
legf_nyelv_eve = programnyelvek[0]["year"]
legf_nyelv = programnyelvek[0]
for programnyelv in programnyelvek:
    if programnyelv["year"] < legf_nyelv_eve:
        legf_auto_eve = programnyelv["year"]
        legf_nyelv = programnyelv

print(f"A legfiatalabb programnyelv: {legf_nyelv}")
