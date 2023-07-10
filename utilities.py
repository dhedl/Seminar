def unos_intervala(min, max):
    while True:
        try:
            broj = int(input(f"Unesite cijeli broj u inervalu {min}-{max}: "))

            if broj < min or broj > max:
                raise Exception(f"Morate upisati broj u intervalu {min}-{max}!")

        except ValueError:
            print('Unijeli ste znak, a ne cijeli broj!')

        except Exception as e:
            print(e)

        else:
            return broj

def unos_cijelog_broja(poruka):
    while True:
        try:
            broj = int(input(poruka))

            if broj < 0:
                raise Exception('Morate upisati cijeli pozitivni broj!')

        except ValueError:
            print('Unijeli ste znak, a ne cijeli broj!')

        except Exception as e:
            print(e)

        else:
            return broj

def unos_realnog_broja(poruka):
    while True:
        try:
            broj = float(input(poruka))

            if broj < 0:
                raise Exception('Morate upisati pozitivni realni broj!')

        except ValueError:
            print('Unijeli ste znak, a ne realni broj!')

        except Exception as e:
            print(e)

        else:
            return broj


def unos_emaila(poruka):
    while True:
        email = input(poruka)

        try:
            email.index("@")

        except ValueError:
            print("Morate unijeti ispravnu email adresu!")

        else:
            return email


def unos_telefona(poruka):
    while True:
        try:
            broj = unos_cijelog_broja(poruka)

            broj_znamenki = str(broj)

            if len(broj_znamenki) > 9:
                raise Exception('Broj mora imati do 10 znamenki!')

        except Exception as e:
            print(e)

        else:
            return str(broj).zfill(10)  # Dodavanje 0 na početak broja


def unos_teksta(poruka):
    while True:
        try:
            tekst = input(poruka)

            if not tekst.isalpha():
                raise Exception("Morate unijeti samo slova!")

        except Exception as e:
            print(e)

        else:
            return tekst