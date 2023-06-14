my_list  = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thrusday', 'Friday' , 'Saturday' , 'Sunday']
print("This is a list : ", my_list)


# tuples are immutable meaning , the elements cannot be altered after declaration
my_tuple = tuple(my_list)
print("This is a tuple : ", my_tuple)

# A set is an unordered collection of data where no duplication is allowed
my_set = set(my_tuple)
print("This is a set : ",my_set)

my_dic = {
    1:"Sunday",
    2:"Monday",
    3:"Tuesday",
    4:"Wednesday",
    5:"Thrusday",
    6:"Friday"}


try:
    a = int(input("pick a number from (1-6)"))
    print("You picked : ", my_dic[a])
except:
    raise
    