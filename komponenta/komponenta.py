from abc import ABC, abstractmethod


class Komponenta(ABC):

    def __init__(self, naziv, snaga, cijena):
        self.__naziv = naziv
        self.__snaga = snaga
        self.__cijena = cijena

    @property
    def naziv(self):
        return self.__naziv

    @naziv.setter
    def naziv(self, naziv):
        self.__naziv = naziv

    @property
    def snaga(self):
        return self.__snaga

    @snaga.setter
    def snaga(self, snaga):
        self.__snaga = snaga

    @property
    def cijena(self):
        return self.__cijena

    @cijena.setter
    def cijena(self, cijena):
        self.__cijena = cijena

    @abstractmethod
    def ispis(self):
        pass
