from abc import ABC , abstractmethod
class Person(ABC):

    def SetProff(self , newProff):
        self.profession = newProff
    @abstractmethod
    def GetProff(self):
        pass

class Teenager(Person):
    def GetProff(self):
        print("Cashier")
class Adult(Person):
    def GetProff(self):
        print("Professor")

Sarah = Teenager()
Jimmy  = Adult()
Sarah.GetProff()
Sarah.SetProff("Saleswoman")
Jimmy.GetProff()
Jimmy.SetProff("CEO")