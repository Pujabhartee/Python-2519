# Working Variables
# syntax ---> var_name = value
# Syntax for text data is to enclose the text inside ' ' or " "
student_name = "Puja"
student_age = 29
student_gpa = 9.11
student_passed = True 

dynamic_variable = 10
#print(dynamic_variable)
print(type(dynamic_variable))

dynamic_variable = 9.5
#print(dynamic_variable)
print(type(dynamic_variable))

dynamic_variable = False
#print(dynamic_variable)
print(type(dynamic_variable))

dynamic_variable = "Hello"
print(type(dynamic_variable))

a = 10
print(id(a))

b = 20
print(id(b))

c = 10
print(id(c))

# List means collection of multiple items -> List is represented using [ ]
a_list = [10,20,30]
#print(type(a_list))
print(id(a_list))

c_list = [10,20,30]
print(id(c_list))


x = "Python "
y = "is "
z = "awesome"

# outut =Python is awesome

# print(xyz)  # NameError: name 'xyz' is not defined

# + (add --> takes multiple numeric values and add them)
# + when used with numerics it's called addition operator
# + when used with text it's called concatenation operator

# what is concatenation? -?> Joining multiple Strings
print(x+y+z) # + as a concatenation operator

x = 10
y = 20
z = 30
print(x+y+z) # + as addition operator

a = "10"
b = "10"

# print(x+a) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(a+b)

# Multiple Variables

x,y,z = 10,20,30 # (LHS=RHS)
# x,y,z = 10,20,30, 40  # ValueError: too many values to unpack (expected 3)
print(x+y+z)

s1,s2,s3 = "orange","apple","cherry"
print(s1,s2+s3)

# using concatenation 
name = "Puja"
age = 25
# print("My name is " +name + "and I am" +age +"years old") # TypeError: can only concatenate str (not "int") to str
print("My name is {name} and I am {age} years old")

# using interpolation
print(f"My name is {name} and I am {age} years old")

# using different dynamic
x,y,z = 10,20,30
print(f"Sum of x,y,z,age: {x+y+z+age}")

# school student info
name = "john"
# class = 8 # SyntaxError: invalid syntax (class is a keyword in python)
school = "DPS"
# print(f"My name is {name}, I am studying in {class} class in {school} school ")

student_name = "john"
student_class = 8
student_school = "DPS"
print(f"My name is {student_name}, I am studying in {student_class} class in {student_school} school ")

