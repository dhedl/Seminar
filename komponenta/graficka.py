from .komponenta import Komponenta


class Graficka(Komponenta):

    def __init__(self, naziv, snaga, cijena, proizvodac):
        super().__init__(naziv, snaga, cijena)
        self.__proizvodac = proizvodac

    @property
    def proizvodac(self):
        return self.__proizvodac

    @proizvodac.setter
    def proizvodac(self, proizvodac):
        self.__proizvodac = proizvodac

    def ispis(self):
      print("Informacije o grafickoj: ")
      print(f'\tNaziv: {self.naziv}')
      print(f'\tSnaga (TDP): {self.snaga}W')
      print(f'\tCijena: {self.cijena}€')
      print(f'\tProizvodac: {self.__proizvodac}')
