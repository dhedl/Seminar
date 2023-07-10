from .komponenta import Komponenta


class SSD(Komponenta):

    def __init__(self, naziv, cijena, kapacitet):
        super().__init__(naziv, None, cijena)
        self.__kapacitet = kapacitet

    @property
    def kapacitet(self):
        return self.__kapacitet

    @kapacitet.setter
    def kapacitet(self, kapacitet):
        self.__kapacitet = kapacitet

    def ispis(self):
        print("Informacije o SSD:")
        print(f'\tNaziv: {self.naziv}')
        print(f'\tCijena: {self.cijena}€')
        print(f'\tKapacitet: {self.__kapacitet}GB')