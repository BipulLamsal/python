#definig a class
# class Dog:
#     pass
# classes name are written in Capitalized form for convention
# THe properties that all Dof objects must have are defined in a method called .__init__()
# .__init__() initializes each new instance of the class.
# we can give .__init__() any number of parameters, but first parameter will alaways be a variable called self.


#updated Class 1
class Dog:
    species = "Canis familiaris"
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age



# the first argument of every class method, including init is always a refrence to the current instance of the class. By convention this argument is always named self.
#  self refers to the newly created object; in other class methods, it refers to the instance whose method was called.

# Attribute created in the .__init__() are caleed instance attributes.
# class attributes are same for all class instances but the instance attributes are different for each instance.

buddy = Dog("Buddy",2)
miles = Dog("Buddy",2)
print(buddy == miles)

# This created two new dog instances. Even though both of them have same name and age.
# they return false while comapring as they are different objects stored in differnt memory locations

# when we instanitate a Dog object, python creates a new instance and passes it to the first parameter of .__init__().
# the attributes can be accessed as

print(buddy.name)
print(miles.age)

# can we access the class attribute?  yes!!!
print(buddy.species)

#can we alter the above value for specefic object?  yes!!!
buddy.species = "ChangedData"
print(buddy.species)

