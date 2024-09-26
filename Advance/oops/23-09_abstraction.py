from abc import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def voice(self):
        pass

class DOG(animal):
    def voice(self):
        return "BHO BHO"

class CAT(animal):
    def voice(self):
        return "MEOW MEOW"

obj = DOG()
print(obj.voice())
obj = CAT()
print(obj.voice())