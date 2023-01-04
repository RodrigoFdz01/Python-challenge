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
