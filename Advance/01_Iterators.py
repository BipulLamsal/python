numbers = [1,2,3,5,6,7,10]
print(dir(numbers))
print(numbers.__iter__().__next__())


#the above code can also be written as :

print(iter(numbers))
print(next(iter(numbers)))

# How is for loop running internally 
# THis is how:
iter_obj = iter(numbers)
while True:
    try:
        element = iter_obj.__next__()
        print(element)
    except StopIteration:
        break

# for element in numbers:
#     print(element)

class Odd:
    def __init__(self,max) :
        self.num = 1
        self.max = max

    def __iter__(self):
        return self
    def __next__(self):
        if self.num <= self.max:
            result = self.num
            self.num = self.num + 2
            return result
        else:
            raise StopIteration


num1 = Odd(10)
iter_num1 = iter(num1)
print(next(num1))
print(next(num1))
print(next(num1))
print(next(num1))
print(next(num1))
print(next(num1))
print(next(num1))
print(next(num1))
print(next(num1))
print(next(num1))
print(next(num1))