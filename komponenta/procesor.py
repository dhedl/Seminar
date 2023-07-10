from .komponenta import Komponenta


class Procesor(Komponenta):

    def __init__(self, naziv, snaga, cijena, socket):
        super().__init__(naziv, snaga, cijena)
        self.__socket = socket

    @property
    def socket(self):
        return self.__socket

    @socket.setter
    def socket(self, socket):
        self.__socket = socket

    def ispis(self):
      print("Informacije o procesoru: ")
      print(f'\tNaziv: {self.naziv}')
      print(f'\tSnaga (TDP): {self.snaga}W')
      print(f'\tCijena: {self.cijena}€')
      print(f'\tSocket: {self.__socket}')
