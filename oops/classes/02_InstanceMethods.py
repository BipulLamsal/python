class Human:
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age
    # Instance method
    def description(self):
        
        return f"{self.name}, who is {self.gender} is {self.age} years old."
    
    
    def say(self, sound):
        return f"{self.name} says {sound}"
    
    def __str__(self) -> str:
        return self.name



person1 = Human("Bipul","male",18)
print(person1)


# methods like -__init__() and .__str__() are called dunder methods because they begin and end with double underscores.
