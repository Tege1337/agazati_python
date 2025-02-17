def read_books(file_path):
    konyvek = []
    with open(file_path, "r", encoding="utf-8") as source:
        for line in source:
            data = line.strip().split(";")
            konyv = {
                "nev": data[0],
                "szul_ev": data[1],
                "halal_ev": data[2],
                "nemzetiseg": data[3],
                "cim": data[4],
                "helyezes": int(data[5])
            }
            konyvek.append(konyv)
    return konyvek

def best_hu_book(konyvek):
    legjobb_konyv = None
    for konyv in konyvek:
        if konyv["nemzetiseg"] == "magyar":
            if legjobb_konyv is None or konyv["helyezes"] < legjobb_konyv["helyezes"]:
                legjobb_konyv = konyv
    return legjobb_konyv

def is_there_ger(konyvek):
    ger_arg = False
    for konyv in konyvek:
        if konyv["nemzetiseg"] == "német":
            ger_arg = True
            break
    
    return ger_arg

def older_than_90(konyvek):
    above_90 = []
    for konyv in konyvek:
        halal_ev = int(konyv["halal_ev"])
        szul_ev = int(konyv["szul_ev"])
        eletkor = konyv[halal_ev] - konyv[szul_ev]
        if eletkor >= 90:
            if konyv["nev"] not in above_90:
                above_90.append(konyv["nev"])

    return above_90

def main():
    file_path = "./konyvek.txt"
    konyvek = read_books(file_path)
    
    print(f"Az állományban {len(konyvek)} db könyv adatai szerepelnek")
    
    legjobb_konyv = best_hu_book(konyvek)
    ger_book = is_there_ger(konyvek)
    kilencven_felett = older_than_90(konyvek)
    
    if legjobb_konyv:
        print(f"A legjobb helyezést elért magyar könyv: {legjobb_konyv['nev']} - {legjobb_konyv['cim']}")

    if ger_book:
        print("A listában van német író.")
    
    print(f"Kilencven év feletti írók: {kilencven_felett}")

if __name__ == "__main__":
    main()