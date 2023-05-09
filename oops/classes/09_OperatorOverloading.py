class Point:
    def __init__(self,x=0,y=0) -> None:
        self.x = x
        self.y = y
        

    def __sub__(self,other):
        self.newx = (self.x - other.x)
        self.newy = (self.y - other.y)

    def square(self):
        self.newx = self.newx ** 2
        self.newy = self.newy ** 2

    def add(self):
        self.distance = self.newx + self.newy
    
    def sqrt(self):
        self.distance = self.distance ** (1/2)
        return self.distance

num1 = Point(6,4)
num2 = Point(2,1)

num1-num2 # this bascially means num1.__sub__(num2)
num1.square()
num1.add()
print(num1.sqrt())




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # overload < operator
    def __lt__(self, other):
        return self.age < other.age

p1 = Person("Alice", 20)
p2 = Person("Bob", 30)

print(p1 < p2)  # prints True
print(p2 < p1)  # prints False






        