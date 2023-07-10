import sqlite3

from korisnik import unos_korisnika, ispis_svih_korisnika
from komponenta import unos_komponente, ispis_svih_komponenti
from utilities import unos_intervala

# Veza s bazom podataka
conn = sqlite3.connect('faks.db')
cursor = conn.cursor()

komponente = []
korisnici = []

running = True
while running:
    print('-' * 20)
    print('1. Unos procesora')
    print('2. Unos grafičke kartice')
    print('3. Unos matične ploče')
    print('4. Unos RAM memorije')
    print('5. Unos SSD')
    print('6. Unos napajanja')
    print('7. Unos korisnika')
    print('8. Ispis svih korisnika')
    print('9. Ispis svih komponenti')
    print('10. Zaustavi program')
    print('-' * 20)

    akcija = unos_intervala(1, 10)

    if akcija == 1:
        komponente.append(unos_komponente("procesor", cursor))
        conn.commit()
    elif akcija == 2:
        komponente.append(unos_komponente("graficka", cursor))
        conn.commit()
    elif akcija == 3:
        komponente.append(unos_komponente("maticna", cursor))
        conn.commit()
    elif akcija == 4:
        komponente.append(unos_komponente("ram", cursor))
        conn.commit()
    elif akcija == 5:
        komponente.append(unos_komponente("ssd", cursor))
        conn.commit()
    elif akcija == 6:
        komponente.append(unos_komponente("napajanje", cursor))
        conn.commit()
    elif akcija == 7:
        korisnici.append(unos_korisnika(cursor))
        conn.commit()
    elif akcija == 8:
        ispis_svih_korisnika(cursor)
    elif akcija == 9:
        ispis_svih_komponenti(cursor)
    elif akcija == 10:
        running = False

conn.close()

# TODO korisniku omogućiti odabir komponenti - sastavljanje konfiguracije, na kraju prikazat konfu i cijenu