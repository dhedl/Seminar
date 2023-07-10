def ispis_svih_korisnika(cursor):
    print("Svi korisnici:")

    query = "SELECT ime, prezime FROM korisnik"
    cursor.execute(query)
    data = cursor.fetchall()

    for d in data:
        print(f"\t{d[0]} {d[1]}")
