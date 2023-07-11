def ispis_konfiguracija(cursor):
    query = "SELECT korisnik.ime, korisnik.prezime, odabrane_komponente.komponente " \
            "FROM odabrane_komponente " \
            "INNER JOIN korisnik ON odabrane_komponente.id_korisnika = korisnik.id"

    cursor.execute(query)
    data = cursor.fetchall()

    for d in data:
        ime = d[0]
        prezime = d[1]
        komponente_ids = d[2].split(',')

        print("\tSastavljena konfiguracija")
        print(f"\tkorisnika: {ime} {prezime}:")
        for komponenta_id in komponente_ids:
            query = f"SELECT naziv FROM komponenta WHERE id = {komponenta_id}"
            cursor.execute(query)
            naziv = cursor.fetchone()[0]
            print(f"\t\t{naziv}")

        # Dohvaćanje ukupne cijene
        query = f"SELECT SUM(cijena) FROM komponenta WHERE id IN ({', '.join(komponente_ids)})"
        cursor.execute(query)
        ukupna_cijena = cursor.fetchone()[0]

        print(f"\tUkupna cijena: {ukupna_cijena:.2f} €")
        print()
