from abc import ABC, abstractmethod

class AbctractAnimal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(AbctractAnimal):
    pass

# obj = Dog()
# Tupeerror
class Dog(AbctractAnimal):
    def speak(self):
        print("гав-гав")

obj = Dog
obj.speak()