# Regular Expressions
# A regular expression or RegEx is a special text string that helps to find patterns in data.
#  A RegEx can be used to check if some pattern exists in a different data type. 
# To use RegEx in python first we should import the RegEx module which is called re.

import re 

#######re.match()
'''
 re.match(): searches only in the beginning of the first line of the string and returns 
 matched objects if found, else returns None.
import re

txt = 'I love to teach python and javaScript'
# It returns an object with span, and match
match = re.match('I love to teach', txt, re.I)
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>

# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (0, 15)

# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 0, 15

substring = txt[start:end]
print(substring)       # I love to teach
'''

#######re.search()
'''
re.search: Returns a match object if there is one anywhere in the string,
 including multiline strings.

import re

txt = 'Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'

# It returns an object with span and match
match = re.search('Pyth', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>

# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (100, 105)

# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 100 105

substring = txt[start:end]
print(substring)       # first
'''

#######re.findall()
'''
re.findall: Returns a list containing all matches

txt = 'Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'

# It return a list
matches = re.findall('language', txt,re.I )
print(matches)  # ['language', 'language']


# If we do not have the re.I flag, then we will have to write our pattern differently.
txt = 'Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'

matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']


matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']
'''


# re.sub: 
'''
# re.sub: Replaces one or many matches within a string
'''


txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
#print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.
# OR
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
#print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.

## 2do ejmeplo
txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
#print(matches)


###### re.split

# re.split: Takes a string, splits it at the match points, returns a list

#txt = '''I am teacher and  I love teaching.
#There is nothing as rewarding as educating and empowering people.
#I found teaching more interesting than any other jobs.
#Does this motivate you to be a teacher?'''
#print(re.split('\n', txt)) # splitting using \n - end of line symbol

##### Exercises: Day 18 #####
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

frequent = re.findall('language', txt,re.I )
print(frequent)  
