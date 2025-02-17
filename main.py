konyvek = []

with open("./konyvek.txt", "r", encoding="utf-8") as source:
    for line in source:
        data = line.strip().split(";")
        konyv = {
            "nev": data[0],
            "szul_ev": data[1], 
            "halal_ev": data[2], 
            "nemzetiseg": data[3], 
            "cim": data[4], 
            "helyezes": int(data[5])  # Számként kezeljük a helyezést az összehasonlításhoz
        }
        konyvek.append(konyv)

print(f"Az állományban {len(konyvek)} db könyv adatai szerepelnek")

legjobb_konyv = None
for konyv in konyvek:
    if konyv["nemzetiseg"] == "magyar":  # Szótár kulcsának használata
        if legjobb_konyv is None or konyv["helyezes"] < legjobb_konyv["helyezes"]:
            legjobb_konyv = konyv

if legjobb_konyv:
    print(f"A legjobb helyezést elért magyar könyv: {legjobb_konyv['nev']} - {legjobb_konyv['cim']}")