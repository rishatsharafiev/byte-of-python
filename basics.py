### Comments
print('hello world')  # Note that print is a function

# Note that print is a function
print('hello world')

# Use as many useful comments as you can in your program to:
# - explain assumptions
# - explain important decisions
# - explain important details
# - explain problems you're trying to solve
# - explain problems you're trying to overcome in your program, etc.
# Code tells you how, comments should tell you why.

### Literal Constants
5
1.23
'This is a string'
"It's a string!"

### Numbers
2
1.23
52.3E-4
# There is no separate long type. The int type can be an integer of any size.

### Strings
'Quote me on this'  # Single Quote

"What's your name?"  # Double Quotes

'''This is a multi-line string. This is the first line.
This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond."
'''  # Triple Quotes

# Strings Are Immutable

### The format method
# indexing
age = 20
name = 'Swaroop'
print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))

# empty
age = 20
name = 'Swaroop'
print('{} was {} years old when he wrote this book'.format(name, age))
print('Why is {} playing with that python?'.format(name))

# named
age = 20
name = 'Swaroop'
print('{name} was {age} years old when he wrote this book'.format(name=name, age=age))
print('Why is {name} playing with that python?'.format(name=name))

# f-strings
age = 20
name = 'Swaroop'
print(f'{name} was {age} years old when he wrote this book')  # notice the 'f' before the string
print(f'Why is {name} playing with that python?')  # notice the 'f' before the string

# detailed specifications
# decimal (.) precision of 3 for float '0.333'
print('{0:.3f}'.format(1.0/3))
# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
print('{0:_^11}'.format('hello'))
# keyword-based 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

# print statement end argument
print('a', end=' ')
print('b', end=' ')
print('c')

### Escape Sequences
print('What\'s your name?')  # escape single quote
print('\\')  # escape backslash itself
print('This is the first line\nThis is the second line')  # new line
print("This is the first sentence. \
This is the second sentence.")  # backslash

### Raw String, mostly for regular expressions
print(r"Newlines are indicated by \n")

# Variable
name = 'Rishat'

# Data types

# Example of variables and data types
i = 5
print(i)
i = i + 1
print(i)
s = '''This is a multi-line string.
This is the second line.'''
print(s)

### Logical And Physical Line
# explicit line joining
a = \
"Hello"

# implicit line joining
vector = {
    'x': 1,
    'y': 2
}

### Indentation
# Use four spaces for indentation. This is the official Python language recommendation.

