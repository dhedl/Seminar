from .komponenta import Komponenta


class Napajanje(Komponenta):

    def __init__(self, naziv, snaga, cijena):
        super().__init__(naziv, snaga, cijena)

    def ispis(self):
      print("Informacije o napajanju: ")
      print(f'\tNaziv: {self.naziv}')
      print(f'\tSnaga: {self.snaga}W')
      print(f'\tCijena: {self.cijena}€')
