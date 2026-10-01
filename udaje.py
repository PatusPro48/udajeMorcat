with open("info.txt", "r", encoding="utf-8") as soubor:
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

        if pohlavi == 'm':
            druh_pohlavi = "sameček"
        elif pohlavi == 'z':
            druh_pohlavi = "samička"
        else:
            druh_pohlavi = "neznámé"

        cena_se_slevou = cena * 0.9

        print(f"{druh_pohlavi} morčete jménem: {jmeno}.")
        print(f"- váží: {hmotnost} g")
        print(f"- datum narození: {datum_narozeni}")
        print(f"- cena se slevou 10%: {cena_se_slevou} kč")
        print("-" * 25)