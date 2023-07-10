from .komponenta import Komponenta


class Maticna(Komponenta):

    def __init__(self, naziv, cijena, socket):
        super().__init__(naziv, None, cijena)
        self.__socket = socket

    @property
    def socket(self):
        return self.__socket

    @socket.setter
    def socket(self, socket):
        self.__socket = socket

    def ispis(self):
      print("Informacije o maticnoj: ")
      print(f'\tNaziv: {self.naziv}')
      print(f'\tCijena: {self.cijena}€')
      print(f'\tSocket: {self.__socket}')
