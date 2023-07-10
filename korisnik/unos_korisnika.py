from utilities import unos_telefona, unos_emaila, unos_teksta
from .korisnik import Korisnik


def unos_korisnika(cursor):

    ime = unos_teksta(f'Unesite ime korisnika: ').capitalize()
    prezime = unos_teksta(f'Unesite prezime korisnika: ').capitalize()
    telefon = unos_telefona(f"Unesite telefon korisnika: ")
    email = unos_emaila(f"Unesite email korisnika: ").strip()

    query = f'''
            INSERT INTO korisnik (ime, prezime, telefon, email)
            VALUES ('{ime}', '{prezime}', '{telefon}', '{email}')
        '''
    cursor.execute(query)

    return Korisnik(ime, prezime, telefon, email)
