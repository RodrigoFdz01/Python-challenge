#import mymodule
#print(mymodule.generate_full_name('Juan', 'GAC'))
#print(mymodule.generate_random())

#from mymodule import Palindromo
#print(Palindromo('ananas'))

from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]

#print(mean(ages))
#print(median(ages))
#print(mode(ages))
#print(stdev(ages))

import cmath
#print(cmath.isclose(50,))
import string
#print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
#print(string.digits)        # 0123456789
#print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

'''
Exercises: Level 1
1-Writ a function which generates a six digit/character random_user_id.
  print(random_user_id());
  '1ee33d'

import random, string
len_password = 6
letters = string.ascii_lowercase
pwd = ''
pwd_len = 6
for i in range(pwd_len):
    random_number = str(int(random.random()*10))
    random_string = random.choice(letters)
    concat = random_number + random_string
    pwd += ''.join(random.choice(concat))
print(pwd)
 -----------2da solucion-------------
import random
import string


alphabet = string.ascii_lowercase + string.digits
password = ''.join(random.choice(alphabet) for i in range(6))

print(password)



2-Modify the previous task. Declare a function named user_id_gen_by_user.
 It doesn’t take any parameters but it takes two inputs using input().
 One of the inputs is the number of characters and the second input is
  the number of IDs which are supposed to be generated

import random, string
how_many = int(input("how many..."))
long = int(input("largo de la password: "))
def random_generator():
    len_password = 6
    letters = string.ascii_lowercase
    pwd = ''
    for i in range(long):
        random_number = str(int(random.random()*10))
        random_string = random.choice(letters)
        concat = random_number + random_string
        pwd += ''.join(random.choice(concat))
    #print(pwd+"--")
    return pwd
for i in range(how_many):
  #random_generator()
    print(random_generator())


3-Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
# rgb(125,244,255) - the output should be in this form

'''
import random
def rgb_color():
    random_red = random.randint(0,255)
    random_green = random.randint(0,255)
    random_blue = random.randint(0,255)
    rgb = [random_red,random_green,random_blue]
    print('A Random color is :',rgb)
    
print(rgb_color())





