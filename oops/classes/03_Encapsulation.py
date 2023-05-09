#Encapsulation refers to the bundling of attributes and methods inside a single class.
# It prevents outer classes from accessing and changing attributes and methods of a class. This also helps to achieve data hiding.

class Bike:
    def __init__(self) -> None:
        self.__maxprice = 900

    def setMaxPrice(self,price):
        self.__maxprice = price

    def sell(self):
        return (f"selling price of the bike : {self.__maxprice}")
    
herohonda = Bike()
print(herohonda.sell())

herohonda.setMaxPrice(2000)
print(herohonda.sell())