import sqlite3

from korisnik import unos_korisnika, ispis_svih_korisnika
from komponenta import unos_komponente, ispis_svih_komponenti, odabir_komponenti, ispis_konfiguracija
from utilities import unos_intervala

# Veza s bazom podataka
conn = sqlite3.connect('faks.db')
cursor = conn.cursor()

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
    print('8. Složi PC')
    print('9. Ispis svih korisnika')
    print('10. Ispis svih komponenti')
    print('11. Ispis konfiguracija')
    print('12. Zaustavi program')
    print('-' * 20)

    akcija = unos_intervala(1, 12)

    if akcija == 1:
        unos_komponente("procesor", cursor)
        conn.commit()
    elif akcija == 2:
        unos_komponente("graficka", cursor)
        conn.commit()
    elif akcija == 3:
        unos_komponente("maticna", cursor)
        conn.commit()
    elif akcija == 4:
        unos_komponente("ram", cursor)
        conn.commit()
    elif akcija == 5:
        unos_komponente("ssd", cursor)
        conn.commit()
    elif akcija == 6:
        unos_komponente("napajanje", cursor)
        conn.commit()
    elif akcija == 7:
        unos_korisnika(cursor)
    elif akcija == 8:
        odabir_komponenti(cursor)
        conn.commit()
    elif akcija == 9:
        ispis_svih_korisnika(cursor)
    elif akcija == 10:
        ispis_svih_komponenti(cursor)
    elif akcija == 11:
        ispis_konfiguracija(cursor)
    elif akcija == 12:
        running = False

conn.close()
