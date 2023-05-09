#  if we need to access the superclass method from the subclass, we use the super() method.

class Human:
    def age (self,num):
        self.age = num
        return self.age

class Male(Human):
    def age (self,num):
        super().age(num)
        return self.age



person1 = Male()
print(person1.age(29))