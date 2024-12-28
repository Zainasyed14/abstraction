from abc import ABC , abstractmethod
class Country(ABC):
    @abstractmethod

    def getCapital(self):
        pass
    def getLangauge(self):
        pass
    def getType(self):
        pass

class Pakistan(Country):
    def getCapital(self):
        print("Islamabad")
    def getLangauge(self):
        print("Urdu")
    def getType(self):
        print("Developing")

class India(Country):
    def getCapital(self):
        print("Dehli")
    def getLangauge(self):
        print("Hindi")
    def getType(self):
        print("Developing")

Pak = Pakistan()
Ind = India()
Ind.getCapital()
Pak.getCapital()