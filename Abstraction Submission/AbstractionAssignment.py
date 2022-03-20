# Python:     Ver 3.10.2
#
# Author:     Fox Addams
#
# Purpose:    Demonstrating the concept of Abstraction via classes & methods.
#
# Tested OS:  This code was written and tested with Windows 10.


# Importing from Abstract Base Class(abc) module 
from abc import ABC, abstractmethod

# Parent Class
class Monopoly(ABC):
    def LTax(self, amount):
        print("Luxury Tax! Pay:",amount)
# Abstract Method
    @abstractmethod
    def PassGo(self, amount):
        pass

    
# Child Class
class TopHat(Monopoly):
# Defining how to implement Abstract Method from Parent Class
    def PassGo(self, amount):
        print('Collect {} salary as you pass GO!'.format(amount))

if __name__ == "__main__":
    player = TopHat()
    player.PassGo("$200")
    player.LTax("$100")









