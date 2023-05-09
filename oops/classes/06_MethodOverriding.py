class Animal:
    def __init__(self,name) -> None:
        self.name = name
    def speak():
        print("Ghrrr")

class Dog(Animal):
    def speak(self):
        print("woof woof")

labrador = Dog("Setu")
labrador.speak()

# if the same method is present in both the superclass and subclass? Method in the subclass overrides the method in superclass


        