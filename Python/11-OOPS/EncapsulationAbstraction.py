print("=============== Example of Encapsulation =====================") 

class parent:
    def __init__(self, var1, var2, var3):
        self.__var1 = var1
        self.__var2 = var2
        self.var3 = var3

    def printValues(self):
        print("Parent Class")
        print(self.__var1, self.__var2)
        self.__printPrivate()

    def __printPrivate(self):
        print("Private Method")

p=parent(4,5,6)
p.printValues()

try:
    print(p.__var1)
except AttributeError as e:
    print("Private attribute are not accessible outside the class")

try:
    print(p.__printPrivateVariable)
except AttributeError as e:
    print("Private methods are not accessible outside the class")


print(p.var3)

print("=============== Example of Abstraction =====================")

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog Barks")

class Cat(Animal):
    def sound(self):
        print("Cat Meows")

dog = Dog()

animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
    print()

try:
    animal = Animal()
    animal.sound()
except TypeError as e:
    print("Animal class is abstract and cannot be instantiated")


