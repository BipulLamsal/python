class Mammal:
    def mammal_info(self):
        print("Mammals can give direct birth.")

class WingedAnimal:
    def winged_animal_info(self):
        print("Winged animals can flap.")
    def common_info(self):
        print("I am inside the Winged Category.")

class WaterAnimal:
    def water_animal_info(self):    
        print("Water Animals can live under water.")
    def common_info(self):
        print("I am inside the Water Animal Category.")

class Bat(Mammal, WingedAnimal):
    pass

class Whale(Mammal,WaterAnimal):
    pass

class WhaleBat(Whale,Bat):
    pass


# create an object of Bat class
b1 = Bat()
b1.mammal_info()
b1.winged_animal_info()


w1 = Whale()
w1.mammal_info()
w1.water_animal_info()

wb1 = WhaleBat()
wb1.common_info()
# for the common methods in two classes the python MRO picks the left method and calls it.


class SuperClass:
    def info (self):
        print("I am the super class.")

class DerivedFirst(SuperClass):
    def info_derived(self):
        print("I am the first derived class.")


class DerivedSecond(DerivedFirst):
    def info_derived_second(self):
        print("I am the second derived class who is derived from the frist derived class.")
    


# class DerivedThird(DerivedFirst,DerivedSecond):
#     pass    this cannot be done.

obj = SuperClass()
obj.info()
obj1 = DerivedFirst()
obj1.info_derived()
obj2 = DerivedSecond()
obj2.info_derived_second()
obj2.info_derived()
obj2.info()

# DerivedSecond inherits all the methods and the attributes of the superclass and derivedfirst class

