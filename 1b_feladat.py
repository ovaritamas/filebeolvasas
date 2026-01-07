programnyelvek = []
with open('adatok\Timeline_of_ programming_languages.csv', 'r', encoding='utf-8') as forrasfajl:
    for i in range(2):
        next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        year = int(adatok[0])
        programming_language = adatok[1]
        first_name = adatok[2]
        last_name = adatok[3]
        programnyelvek.append([year, programming_language, first_name, last_name])

"""Legfiatalabb nyelv"""
legf_nyelv_eve = programnyelvek[0][0]
legf_nyelv = programnyelvek[0]
for programnyelv in programnyelvek:
    if programnyelv[0] > legf_nyelv_eve:
        legf_nyelv_eve = programnyelv[0]
        legf_nyelv = programnyelv

print(f"A legfiatalabb programnyelv: {legf_nyelv}")

"""Legidősebb nyelv"""
legid_nyelv_eve = programnyelvek[0][0]
legid_nyelv = programnyelvek[0]
for programnyelv in programnyelvek:
    if programnyelv[0] < legid_nyelv_eve:
        legid_nyelv_eve = programnyelv[0]
        legid_nyelv = programnyelv

print(f"A legidősebb programnyelv: {legid_nyelv}")
