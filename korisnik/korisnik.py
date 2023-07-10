class Korisnik():

    def __init__(self, ime, prezime, telefon, email):
        self.__ime = ime
        self.__prezime = prezime
        self.__telefon = telefon
        self.__email = email

    @property
    def ime(self):
        return self.__ime

    @ime.setter
    def ime(self, ime):
        self.__ime = ime

    @property
    def prezime(self):
        return self.__prezime

    @prezime.setter
    def prezime(self, prezime):
        self.__prezime = prezime

    @property
    def telefon(self):
        return self.__telefon

    @telefon.setter
    def telefon(self, telefon):
        self.__telefon = telefon

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    def ispis(self):
      print("Informacije o korisniku: ")
      print(f'\tIme: {self.ime}')
      print(f'\tPrezime: {self.prezime}')
      print(f'\tTelefon: {self.telefon}')
      print(f'\tEmail: {self.email}')
