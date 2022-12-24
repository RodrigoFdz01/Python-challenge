countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5]
'''
# funcion como param
def sum_numbers(nums):  
    return sum(nums)    

def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation


result = higher_order_function(sum_numbers, [4, 5])
#print(result)       # 9

####       Function as a Return Value

def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3
#######     Python Closures

def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
#print(closure_result(5))  # 15



############  decoradores-python


# creando un decorador

# Normal function
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON

## Let us implement the example above with a decorator

This decorator function is a higher order function
that takes a function as a parameter
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON




#########################   Built-in Higher Order Functions
#Some of the built-in higher order functions that we cover in this 
# part are map(), filter, and reduce.

#############  Map Function

#ejemplo 1
numbers = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x * 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]

# Lo mismo pero con una lambda function
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]


#ejemplo 2

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(tuple(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# Lo mismo pero con una lambda function
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']



#############  Filter Function

numbers = [1, 2, 3, 4, 5]  # iterable
def is_odd(num):
    if num % 2 != 0:
        return True
    return False

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))       # [1, 3, 5]

#############  Reduce Function

from functools import reduce
numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15


##### Exercises: Day 14-High order functions  ########

#The filter() function calls the specified function which returns boolean for each item of the specified iterable (list).

#The map() function is a built-in function that takes a function and iterable as parameters.

#The reduce() like map and filter it takes two parameters, a function and an iterable. However, it does not return another iterable, instead it returns a Single value




###  Exercises
# 1 - Use map to create a new list by changing each country to uppercase in the countries list

def to_upper(name):
    return name.upper()

names_upper = map(to_upper,countries)
#print(list(names_upper))

# 2 - Use map to create a new list by changing each number to its square in the numbers list
def to_square(number):
    return number ** 2

numbers_squared = map(to_square, numbers)    
#print(list(numbers_squared))

# 3 - Use filter to filter out countries containing 'land'.
def filter_func():
    for i in countries:
        if "lan" in i:
            print (i)  
#filter_func()

# 4 - Use filter to filter out countries having exactly six characters.

def filter_chars():
    for i in countries:
        if (len(i)) == 6:
            print(i)
#filter_chars()

# 5 - Use filter to filter out countries starting with an 'E'
def filter_e():
    for i in countries:
        if (i[0]) == "E":
            print(i)
#filter_e()

# 6 - Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
### ???????

# 7 - Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.

countries_and = ['Sweden',2, 'Norway',True,44, "bokee"]

def get_string_lists(param):
    for i in param:
        if type(i) == str:
            print(i)
#return only string items

get_string_lists(countries_and)


# 8 - Use reduce to sum all the numbers in the numbers list.

from functools import reduce

def sum_nums(x, y):
    return int(x) + int(y)

total2 = reduce(sum_nums, numbers)
print(total2)    # 15

# 9 - Use reduce to concatenate all the countries and to produce this sentence:
#  Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

##### casi ###############
##### casi ###############
##### casi ###############
from functools import reduce


def concatenate_countries():
    string = " are north European countries"
    last_el = str(countries[:-1])
    rest = "and " + countries[-1]
    print(last_el+", " + rest + string)
        
print(concatenate_countries())
'''

# 10 - Declare a function called categorize_countries that returns a list of countries
#  with some common pattern (you can find the countries list in this repository as 
# countries.js (eg 'land', 'ia', 'island', 'stan')).

countries = [ 'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola',
 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 
 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize',
  'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 
  'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 
  'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 
  'China', 'Colombi', 'Comoros', 'Congo (Brazzaville)', 'Congo', 
  'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 
  'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic'];


  # 11 - Create a function returning a dictionary, where keys stand for starting letters of countries 
  # and values are the number of country names starting with that letter.