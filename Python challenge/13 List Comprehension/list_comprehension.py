####  List comprehension

###  if you want to generate a list of numbers
numbers = [i for i in range(5)]  # to generate numbers 
#print(numbers)                    # [0, 1, 2, 3, 4]
 # It is possible to do mathematical operations during iteration
squares = [i * i for i in range(5)]
#print(squares)                    # [0, 1, 4, 9, 16]
# It is also possible to make a list of tuples
numbers = [(i, i * i) for i in range(5)]
#print(numbers)   # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]


####  List comprehension can be combined with if expression

# Generating even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]  # to generate even numbers list in range 0 to 21
#print(even_numbers)                    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Generating odd numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]  # to generate odd numbers in range 0 to 21
#print(odd_numbers)                      # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in range(21) if i % 2 == 0 and i > 0]
#print(positive_even_numbers)                    # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Flattening a three dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
#print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]


add_two_nums = lambda a, b: a + b
#print(add_two_nums(2,3)) 
 
#print((lambda a, b: a + b)(3,3))

square = lambda x : x ** 2
#print(square(3))  

# Multiple variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
#print(multiple_variable(5, 5, 3)) # 22

########## Lambda Function Inside Another Function

def power(x):
    return lambda n : x * n

cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
#print(cube)          # 8


##### Exercises: Day 13- List Comprehension ########

# 1-Filter only negative and zero in the list using list comprehension

numbers3 = [-4, -3, -2, -1, 0, 2, 4, 6]

neg_zero_numbs = [i for i in numbers3 if i <= 0  ]
#print(neg_zero_numbs)


# 2- Flatten the following list of lists to a one dimensional list :
list_of_lists2 =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]] ## [1, 2, 3, 4, 5, 6, 7, 8, 9]

flattened_li = [number for row in list_of_lists2 for number in row]


print(flattened_li)


#  3- Using list comprehension to create the following list of tuples:

[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]


# 4- Flatten the following list to a new list:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

new_list2 = [list(name) for row in countries for name in row]
#print(new_list2)


# 5 - Change the following list to a list of dictionaries:

countries3 = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#output: [{'country': 'FINLAND', 'city': 'HELSINKI'},
#           {'country': 'NORWAY', 'city': 'OSLO'}]

new_list3 = [f'{name: name}' for row in countries3 for name in row]
#print(new_list3)



# 6 - Change the following list of lists to a list of concatenated strings:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# output ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

names2 = [f'{name[0]} {name[1]}'  for row in names for name in row]
#print(names2)
