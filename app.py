# we can run code by using python lib/app.py in the cli
print('Herro world!', end='') # tells the interperter to not create a new line.
print('Herro sun!', end='!! ')
print('Herro sky!', end='!!!\n') # \n creates a new line
print('Herro moon!')

# if you're in cli using python, use 'exit()' or control+d to exit.

# STRINGS
str('imma string!')

cat_name = 'Chloe'
print(f'Say hullo to my cat {cat_name}')

#! NOTE: Backticks in Python are not valid characters, so don't use backticks ( ` ) for strings in Python.

price_1 = 3
price_2 = 2.5

print(f"Item 1 costs ${price_1:.2f}")
# => Item 1 costs $3.00
print(f"Item 2 costs ${price_2:.2f}")
# => Item 2 costs $2.50

"hello"
# "hello"
"hello".upper()
# "HELLO"
"HELLO".lower()
# "hello"
"hello".capitalize()
# "Hello"
"hello" + "world"
# "helloworld"
"hello" * 3
# "hellohellohello"

type("hello")
# => <class 'str'>

dir("hello")
# => ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', ... ]

# NUMBERS
int("1")
# => 1
int(1.1)
# => 1
float("1.1")
# => 1.1

4 / 3
# 1.3333333333333333
4 / 3.0
# 1.3333333333333333
float(4 / 3)
# 1.3333333333333333

### Sequence Types
## Lists
[1, 3, 400, 7]
# => [1, 3, 400, 7]
list()
# => []

# access a specific element in a list via index
list_abc = ['a','b','c']
list_abc[0]
# => 'a'
list_abc[1]
# => 'b'
list_abc[2]
# => 'c'

# iterating over lists
len([1, 3, 400, 7])
# 4
sorted([5, 100, 234, 7, 2])
# [2, 5, 7, 100, 234]
list_123 = [1, 2, 3]
list_123.pop()
# 3
list_123.remove(1)
print(list_123)
# [2]

## Tuples
# different from lists 
#! 1. inside of () instead of brackets.
#! 2. immutable!
# use case: when data should be read-only (t.ex: for retrieval in a db)

# The tuple() class constructor function can also be used to cast lists and other iterable data types to tuples.
# n.b. NOTE: Parentheses can also be used for order of operations and grouping statements. To let Python know that it's looking at a tuple, there has to be at least one comma- even in tuples with only one element: (1,).

(1, 2, 3)
# => (1, 2, 3)
tuple([1, 2, 3])
# => (1, 2, 3)

# ... see next lecture