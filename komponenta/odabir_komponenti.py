from utilities import unos_intervala
from korisnik import ispis_svih_korisnika


def odabir_komponenti(cursor):
    # Dohvaćanje broja korisnika iz baze
    query = "SELECT COUNT(*) FROM korisnik"
    cursor.execute(query)
    broj_korisnika = cursor.fetchone()[0]

    if broj_korisnika == 0:
        print("Nema dostupnih korisnika! Unesi korisnika prvo!")
        return  # Izlaz iz funkcije ako nema korisnika

    print("Dostupni korisnici:")
    ispis_svih_korisnika(cursor)

    odabrani_korisnik_id = unos_intervala(1, broj_korisnika)

    # Provjera da li konfiguracija za odabranog korisnika već postoji
    query = f"SELECT komponente FROM odabrane_komponente WHERE id_korisnika = {odabrani_korisnik_id}"
    cursor.execute(query)
    existing_config = cursor.fetchone()

    if existing_config:
        print("Konfiguracija za odabranog korisnika već postoji!")
        return  # Izlaz iz funkcije ako korisnik već ima konfiguraciju

    # Ispis i odabir procesora
    print("Odaberite procesor:")
    query = "SELECT * FROM komponenta INNER JOIN procesor ON komponenta.id = procesor.id_komponente"
    cursor.execute(query)
    data = cursor.fetchall()
    for i, d in enumerate(data, start=1):
        id_komponente, naziv, cijena, snaga, socket = d[0], d[1], d[2], d[5], d[6]
        print(f"{i}. {naziv} - Snaga: {snaga}W - Socket: {socket} - Cijena: {cijena}€")

    odabir_procesora = unos_intervala(1, len(data))
    odabrani_procesor = data[odabir_procesora - 1]
    id_komponente = odabrani_procesor[0]
    query = f"INSERT INTO odabrane_komponente (id_korisnika, komponente) " \
            f"VALUES ({odabrani_korisnik_id}, '{id_komponente}')"
    cursor.execute(query)

    # Ispis i odabir grafičke kartice
    print("Odaberite grafičku karticu:")
    query = "SELECT * FROM komponenta INNER JOIN graficka ON komponenta.id = graficka.id_komponente"
    cursor.execute(query)
    data = cursor.fetchall()
    for i, d in enumerate(data, start=1):
        id_komponente, naziv, cijena, snaga, proizvodac = d[0], d[1], d[2], d[5], d[6]
        print(f"{i}. {naziv} - Snaga: {snaga}W - Proizvođač: {proizvodac} - Cijena: {cijena}€")

    odabir_graficke = unos_intervala(1, len(data))
    odabrana_graficka = data[odabir_graficke - 1]
    id_komponente = odabrana_graficka[0]
    query = f"UPDATE odabrane_komponente SET komponente = komponente || ',{id_komponente}'" \
            f" WHERE id_korisnika = {odabrani_korisnik_id}"
    cursor.execute(query)

    # Ispis i odabir RAM memorije
    print("Odaberite RAM memoriju:")
    query = "SELECT * FROM komponenta INNER JOIN ram ON komponenta.id = ram.id_komponente"
    cursor.execute(query)
    data = cursor.fetchall()
    for i, d in enumerate(data, start=1):
        id_komponente, naziv, cijena, kapacitet = d[0], d[1], d[2], d[5]
        print(f"{i}. {naziv} - Kapacitet: {kapacitet}GB - Cijena: {cijena}€")

    odabir_ram = unos_intervala(1, len(data))
    odabrana_ram = data[odabir_ram - 1]
    id_komponente = odabrana_ram[0]
    query = f"UPDATE odabrane_komponente SET komponente = komponente || ',{id_komponente}' " \
            f"WHERE id_korisnika = {odabrani_korisnik_id}"
    cursor.execute(query)

    # Ispis i odabir SSD diska
    print("Odaberite SSD disk:")
    query = "SELECT * FROM komponenta INNER JOIN ssd ON komponenta.id = ssd.id_komponente"
    cursor.execute(query)
    data = cursor.fetchall()
    for i, d in enumerate(data, start=1):
        id_komponente, naziv, cijena, kapacitet = d[0], d[1], d[2], d[5]
        print(f"{i}. {naziv} - Kapacitet: {kapacitet}GB - Cijena: {cijena}€")

    odabir_ssd = unos_intervala(1, len(data))
    odabrani_ssd = data[odabir_ssd - 1]
    id_komponente = odabrani_ssd[0]
    query = f"UPDATE odabrane_komponente SET komponente = komponente || ',{id_komponente}'" \
            f" WHERE id_korisnika = {odabrani_korisnik_id}"
    cursor.execute(query)

    # Ispis i odabir napajanja
    print("Odaberite napajanje:")
    query = "SELECT * FROM komponenta INNER JOIN napajanje ON komponenta.id = napajanje.id_komponente"
    cursor.execute(query)
    data = cursor.fetchall()
    for i, d in enumerate(data, start=1):
        id_komponente, naziv, cijena, snaga = d[0], d[1], d[2], d[5]
        print(f"{i}. {naziv} - Snaga: {snaga}W - Cijena: {cijena}€")

    odabir_napajanja = unos_intervala(1, len(data))
    odabrano_napajanje = data[odabir_napajanja - 1]
    id_komponente = odabrano_napajanje[0]
    query = f"UPDATE odabrane_komponente SET komponente = komponente || ',{id_komponente}'" \
            f" WHERE id_korisnika = {odabrani_korisnik_id}"
    cursor.execute(query)

    # Ispis i odabir matične ploče
    print("Odaberite matičnu ploču:")
    query = f"SELECT * FROM komponenta INNER JOIN maticna ON komponenta.id = maticna.id_komponente" \
            f" WHERE socket = '{odabrani_procesor[6]}'"
    cursor.execute(query)
    data = cursor.fetchall()
    for i, d in enumerate(data, start=1):
        id_komponente, naziv, cijena, socket = d[0], d[1], d[2], d[5]
        print(f"{i}. {naziv} - Socket: {socket} - Cijena: {cijena}€")

    odabir_mbo = unos_intervala(1, len(data))
    odabrana_mbo = data[odabir_mbo - 1]
    id_komponente = odabrana_mbo[0]
    query = f"UPDATE odabrane_komponente SET komponente = komponente || ',{id_komponente}' " \
            f"WHERE id_korisnika = {odabrani_korisnik_id}"
    cursor.execute(query)

    # Dohvaćanje korisnika
    query = f"SELECT ime, prezime FROM korisnik WHERE id = {odabrani_korisnik_id}"
    cursor.execute(query)
    korisnik = cursor.fetchone()
    ime, prezime = korisnik[0], korisnik[1]

    # Dohvaćanje konfiguracije
    query = f"SELECT komponente FROM odabrane_komponente WHERE id_korisnika = {odabrani_korisnik_id}"
    cursor.execute(query)
    konfiguracija_ids = cursor.fetchone()[0].split(',')

    # Dohvaćanje naziva komponenti
    query = f"SELECT naziv FROM komponenta WHERE id IN ({', '.join(konfiguracija_ids)})"
    cursor.execute(query)
    komponente = cursor.fetchall()

    print("\tSastavljena konfiguracija")
    print(f"\tkorisnika {ime} {prezime}:\n")
    for komponenta in komponente:
        print(f"\t{komponenta[0]}")

    # Dohvaćanje cijena komponenti
    query = f"SELECT ROUND(SUM(cijena), 2) FROM komponenta WHERE id IN ({', '.join(konfiguracija_ids)})"
    cursor.execute(query)
    ukupna_cijena = cursor.fetchone()[0]

    print(f"Ukupna cijena: {ukupna_cijena} €")

