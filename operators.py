### Operators

### Shortcut for math operation and assignment
a = 2
a = a * 3

a = 2
a *= 3

### Evaluation Order
# Operator	Description
# lambda	Lambda expression
# if – else	Conditional expression
# or	Boolean OR
# and	Boolean AND
# not x	Boolean NOT
# in, not in, is, is not, <, <=, >, >=, !=, ==	Comparisons, including membership tests and identity tests
# |	Bitwise OR
# ^	Bitwise XOR
# &	Bitwise AND
# <<, >>	Shifts
# +, -	Addition and subtraction
# *, @, /, //, %	Multiplication, matrix multiplication, division, floor division, remainder [5]
# +x, -x, ~x	Positive, negative, bitwise NOT
# **	Exponentiation [6]
# await x	Await expression
# x[index], x[index:index], x(arguments...), x.attribute	Subscription, slicing, call, attribute reference
# (expressions...), [expressions...], {key: value...}, {expressions...}	Binding or tuple display, list display, dictionary display, set display

### Changing the Order Of Evaluation
# use parentheses

### Associativity
# Operators are usually associated from left to right


### Expressions
length = 5
breadth = 2
area = length * breadth
print('Area is', area)
print('Perimeter is', 2 * (length + breadth))