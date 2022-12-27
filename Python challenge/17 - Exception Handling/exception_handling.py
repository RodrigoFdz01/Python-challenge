
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2022 - year_born
    print(f'You are {name}. And your age is {age}.')
except:
    print('Something went wrong')

try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)




####### Packing and Unpacking Arguments in Python  #######

 # We use two operators:

# * for tuples  and ** for dictionaries

numbers = range(2, 7)  # normal call with separate arguments
#print(list(numbers)) # 

args = [2, 7]
numbers = range(*args)  # call with arguments unpacked from a list
print(numbers)      # [2, 3, 4, 5,6]
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, a, *rest = countries
print(fin, sw, a, rest)  # Finland Sweden Norway ['Denmark', 'Iceland']



# Unpacking Dictionaries

def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} years old.'

dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
#print(unpacking_person_info(**dct)) 
# Asabeneh lives in Finland, Helsinki. He is 250 years old.

#### Packing ####
#Sometimes we never know how many arguments need to be passed to a python function. We can use the packing method to allow our function to take unlimited number or arbitrary number of arguments.

###Packing Lists 

def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
#print(sum_all(1, 2, 3))             # 6
#print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28


###  Packing Dictionaries

def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
	# Printing dictionary items
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Asabeneh",
 country="Finland", city="Helsinki", age=250))
 name = Asabeneh
 country = Finland
 city = Helsinki
 age = 250
 {'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}


#### Spreading in Python

lst_one = [1, 2, 3]
lst_two = [4, 5, 6]
lst = [ *lst_one, *lst_two]
# print(lst) [1,2,3,4,5,6] 

### Enumerate
# If we are interested in an index of a list, we use enumerate built-in function to get the index of each item in the list.


# for index, i in enumerate(countries):
    # print('hi')
    # if i == 'Finland':
        # print(f'The country {i} has been found at index {index}')


# for index, item in enumerate([20, 30, 40]):
    # print(index, item)

###  Zip
#Sometimes we would like to combine lists when looping through them.
#  See the example below:    

fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

#print(fruits_and_veges)

      ####   Exercises: Day 16 ####


# Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']


*nordic_countries,es,ru = names

print(nordic_countries)
print(es)
print(ru)
