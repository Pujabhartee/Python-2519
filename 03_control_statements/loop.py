# while loop
# syntax
# while condition:
#     code to repeat

count = 1
while count <= 5:
    print(count)
    count += 1


# Simulate real wold use case for while
atm_correct_pin = 1234
user_given_pin = 0

while user_given_pin != atm_correct_pin:
    user_given_pin = int(input("Enter PIN: "))

print("You can Withdraw")

# # Infinite Loop
# count = 1
# while True:
#     print(count)
#     count += 1

# for loop : used to iterate over a Sequence
# Syntax
# for elements in Sequence:
#     statements

text = "python is a general purpose language"
for character in text:
    print(character)

# num = 10
# for character in num:
#     print(character)  # TypeError: 'int' object is not iterable

# Test to check given object is iterable --> __iter__
num = 10
print(type(num))
print(dir(num)) # '__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']

text = "python"
print(type(text))
print(dir(text)) # ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

list_nums = [10,20,30]
print(type(list_nums))
print(dir(list_nums)) # ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
for num in list_nums:
    print(num)

# for loop : repeat block of code, if you know number of iterations in advance

print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")

# range()
for num in range(10):
    print(num)

for num in range(10):
    print("Hi")

for num in range(1,6):
    print(num)

for num in range(1,6,1):
    print(num)

for num in range(2,10,2):
    print(num)

# for num in range(2,10,2,2):   #TypeError: range expected at most 3 arguments, got 4
#     print(num) 

for num in range(1,10,1):
    print(num)

# reverse indexing
for num in range(10,1,-1):
    print(num)

for num in range(10,1,-2):
    print(num)

# get even numbers
print("printing even numbers from 1 to 20")
num = 2
while num <= 20:
    print(num)
    num += 2

# get even numbers
#Loop with condition
print("printing even numbers from 1 to 20")
num = 2
while num <= 20:
    if num% 2 == 0:
        print(num)
    num += 1

# get even numbers
print("printing even numbers from 1 to 20")
for num in range(2,22,2):
    print(num)

# List of courses 
courses_list = ["python", "cloud","devops","ai"]
for course in courses_list:
    print(course)


# Nested Loops
for i in range(1,4):
    for j in range(1,4):
        print(f" {i} * {j} = {i*j}")
    print("-----")

# Nested Loops
i = 1
while i < 4:
    j=1
    while j < 4:
        print(f" {i} * {j} = {i*j}")
        j += 1
    print("-----")
    i += 1


# Branching Statements (Jump Statements)

# break : exits the loop entirely
for num in range(5):
    if num == 3:
        break # loop will terminate here
    print(num)

# continue : skips the current iteration and continue the loop 
for num in range(5):
    if num == 3:
        continue # skip this current iteration 
    print(num)

# pass : does nothing, generally used as place holder
if 5>9:
    pass # (if we left blank we get error)

# pass : use for future
for num in range(5):
    if num == 3:
        pass # keep code here in future
    print(num)
