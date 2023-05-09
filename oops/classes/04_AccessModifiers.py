# Encapsulation can be achieved by declaring the data members and methods of a class either as private or protected. But In Python, we don’t have direct access modifiers like public, private, and protected. We can achieve this by using single underscore and double underscores.
# Three basic types of the access modifiers in python are :
# 1.public member - accessible anywhere outside of the class.
# 2.private member - accessible within the class.
# 3.protected member - accessible within the class and its derived classes


#public member

class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data members
        self.name = name
        self.salary = salary

    # public instance methods
    def show(self):
        # accessing public data member
        print("Name: ", self.name, 'Salary:', self.salary)

# creating object of a class
emp = Employee('Bipul', 10000)

# accessing public data members
print("Name: ", emp.name, 'Salary:', emp.salary)

# calling public method of the class
emp.show()


#private memeber:
class Student:
    def __init__(self,name,percentage) :
        self.name = name
        self.__percentage = percentage

# the private memeber can be accessed using the public instance method
    def show(self):
        return f"Name: {self.name} Percentage: {self.__percentage}"

student1 = Student('Bipul',95)
# print(f"Percentage of {student1.name} is {student1.__percentage}")
print(student1.show())

# another way to access the private memeber of the class is by mangling

print(f"Percentage of {student1.name} is {student1._Student__percentage}")


class Company:
    def __init__(self) -> None:
        self._project = "Low Level Langauge"

class Coder(Company):
    def __init__(self,name) -> None:
        self.name = name
        Company.__init__(self)

    def show(self):
        print("Coder name : ",self.name)
        print("Working on the project : ",self._project)

c1 = Coder("Bipul")
c1.show()
        

        

