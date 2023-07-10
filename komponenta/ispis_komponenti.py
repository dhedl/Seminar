from komponenta import Procesor, Graficka, Maticna, RAM, SSD, Napajanje


def ispis_svih_komponenti(cursor):
    print(f'-' * 20, "Procesori", '-' * 20)
    query = "SELECT * FROM komponenta INNER JOIN procesor ON komponenta.id = procesor.id_komponente"
    cursor.execute(query)
    data = cursor.fetchall()
    for d in data:
        id_komponente, naziv, cijena, snaga, socket = d[0], d[1], d[2], d[5], d[6]
        komponenta = Procesor(naziv, snaga, cijena, socket)
        komponenta.ispis()

    print(f'-' * 20, "Grafičke kartice", '-' * 20)
    query = "SELECT * FROM komponenta INNER JOIN graficka ON komponenta.id = graficka.id_komponente"
    cursor.execute(query)
    data = cursor.fetchall()
    for d in data:
        id_komponente, naziv, cijena, snaga, proizvodac = d[0], d[1], d[2], d[5], d[6]
        komponenta = Graficka(naziv, snaga, cijena, proizvodac)
        komponenta.ispis()

    print(f'-' * 20, "Matične ploče", '-' * 20)
    query = "SELECT * FROM komponenta INNER JOIN maticna ON komponenta.id = maticna.id_komponente"
    cursor.execute(query)
    data = cursor.fetchall()
    for d in data:
        id_komponente, naziv, cijena, socket = d[0], d[1], d[2], d[5]
        komponenta = Maticna(naziv, cijena, socket)
        komponenta.ispis()

    print(f'-' * 20, "RAM memorije", '-' * 20)
    query = "SELECT * FROM komponenta INNER JOIN ram ON komponenta.id = ram.id_komponente"
    cursor.execute(query)
    data = cursor.fetchall()
    for d in data:
        id_komponente, naziv, cijena, kapacitet = d[0], d[1], d[2], d[5]
        komponenta = RAM(naziv, cijena, kapacitet)
        komponenta.ispis()

    print(f'-' * 20, "SSD diskovi", '-' * 20)
    query = "SELECT * FROM komponenta INNER JOIN ssd ON " \
            "komponenta.id = ssd.id_komponente"
    cursor.execute(query)
    data = cursor.fetchall()
    for d in data:
        id_komponente, naziv, cijena, kapacitet = d[0], d[1], d[2], d[5]
        komponenta = SSD(naziv, cijena, kapacitet)
        komponenta.ispis()

    print(f'-' * 20, "Napajanja", '-' * 20)
    query = "SELECT * FROM komponenta INNER JOIN napajanje ON komponenta.id = napajanje.id_komponente"
    cursor.execute(query)
    data = cursor.fetchall()
    for d in data:
        id_komponente, naziv, cijena, snaga = d[0], d[1], d[2], d[5]
        komponenta = Napajanje(naziv, snaga, cijena)
        komponenta.ispis()