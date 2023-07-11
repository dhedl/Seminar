def ispis_svih_korisnika(cursor):

    query = "SELECT ime, prezime FROM korisnik"
    cursor.execute(query)
    data = cursor.fetchall()

    if not data:
        print("Nema dostupnih korisnika! Unesi korisnika prvo!")
    else:
        print("Svi korisnici:")
        for i, d in enumerate(data, start=1):
            print(f"\t{i}. {d[0]} {d[1]}")
