from komponenta import Graficka, RAM, Napajanje, Maticna, Procesor, SSD
from utilities import unos_cijelog_broja, unos_realnog_broja


def unos_komponente(tip, cursor):
    naziv = input("Unesite naziv komponente: ").upper()
    cijena = unos_realnog_broja("Unesite cijenu komponente: ")

    if tip == "procesor":
        snaga = unos_cijelog_broja("Unesite snagu procesora: ")
        socket = input("Unesite socket procesora: ")

        query1 = f'''
                    INSERT INTO komponenta (naziv, cijena)
                    VALUES ('{naziv}', {cijena})
                '''
        cursor.execute(query1)
        id_komponente = cursor.lastrowid
        query2 = f'''
                    INSERT INTO procesor (id_komponente, snaga, socket)
                    VALUES ({id_komponente}, {snaga}, '{socket}')
                '''
        cursor.execute(query2)

        return Procesor(naziv, snaga, cijena, socket.upper())

    elif tip == "graficka":
        proizvodac = input("Unesite proizvođača grafičke kartice: ")
        snaga = unos_cijelog_broja("Unesite snagu grafičke kartice: ")

        query1 = f'''
                    INSERT INTO komponenta (naziv, cijena)
                    VALUES ('{naziv}', {cijena})
                '''
        cursor.execute(query1)
        id_komponente = cursor.lastrowid
        query2 = f'''
                    INSERT INTO graficka (id_komponente, snaga, proizvodac)
                    VALUES ({id_komponente}, {snaga},'{proizvodac}')
                '''
        cursor.execute(query2)

        return Graficka(naziv, snaga, cijena, proizvodac.upper())

    elif tip == "maticna":
        socket = input("Unesite socket matične ploče: ")

        query1 = f'''
                    INSERT INTO komponenta (naziv, cijena)
                    VALUES ('{naziv}', {cijena})
                '''
        cursor.execute(query1)
        id_komponente = cursor.lastrowid
        query2 = f'''
                    INSERT INTO maticna (id_komponente, socket)
                    VALUES ({id_komponente}, '{socket}')
                '''
        cursor.execute(query2)

        return Maticna(naziv, cijena, socket.upper())

    elif tip == "ram":
        kapacitet = unos_cijelog_broja("Unesite kapacitet RAM memorije (u GB): ")

        query1 = f'''
                    INSERT INTO komponenta (naziv, cijena)
                    VALUES ('{naziv}', {cijena})
                '''
        cursor.execute(query1)
        id_komponente = cursor.lastrowid
        query2 = f'''
                    INSERT INTO ram (id_komponente, kapacitet)
                    VALUES ({id_komponente}, {kapacitet})
                '''
        cursor.execute(query2)

        return RAM(naziv, cijena, kapacitet)

    elif tip == "ssd":
        kapacitet = unos_cijelog_broja("Unesite kapacitet SSD memorije (u GB): ")

        query1 = f'''
                    INSERT INTO komponenta (naziv, cijena)
                    VALUES ('{naziv}', {cijena})
                '''
        cursor.execute(query1)
        id_komponente = cursor.lastrowid
        query2 = f'''
                    INSERT INTO ssd (id_komponente, kapacitet)
                    VALUES ({id_komponente}, {kapacitet})
                '''
        cursor.execute(query2)

        return SSD(naziv, cijena, kapacitet)

    elif tip == "napajanje":
        snaga = unos_cijelog_broja("Unesite snagu napajanja (u W): ")

        query1 = f'''
                    INSERT INTO komponenta (naziv, cijena)
                    VALUES ('{naziv}', {cijena})
                '''
        cursor.execute(query1)
        id_komponente = cursor.lastrowid
        query2 = f'''
                    INSERT INTO napajanje (id_komponente, snaga)
                    VALUES ({id_komponente}, {snaga})
                '''
        cursor.execute(query2)

        return Napajanje(naziv, cijena, snaga)

    else:
        raise ValueError("Nepoznat tip komponente.")

