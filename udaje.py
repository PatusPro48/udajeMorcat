def morcata(info.txt):
    with open(info.txt, "r", encoding="utf-8") as soubor:
        for radek in soubor:
            radek = radek.strip()
            if not radek:
                continue

            casti = radek.split(';')
            if len(casti) != 5:
                print(f"Neplatný formát řádku: {radek}")
                continue

            jmeno = casti[0]
            hmotnost = int(casti[1])
            datum_narozeni = casti[2]
            cena = float(casti[3])
            pohlavi = casti[4].lower()