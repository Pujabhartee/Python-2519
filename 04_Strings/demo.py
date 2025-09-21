# Strings
s1 = 'data'
s2 = "data"
s3 = '''data'''
s4 = """data"""
print(s1)
print(s2)
print(s3)
print(s4)

print(type(s1))
print(type(s2))
print(type(s3))
print(type(s4))

# Multi Line Strings
# mls = "this is a very
# big line of strings"   # SyntaxError: unterminated string literal 
# print(mls)

mls = '''this is a very
big line of strings
more lines
more lines'''   # or """ .... """
print(mls)

# ' inside a string
question = "how are you?"
# answer = 'I'm fine'  # SyntaxError: unterminated string literal 
answer = "I'm fine"
print(answer)

# answer = "doing "great"."  # SyntaxError: invalid syntax
answer = 'doing "great".'
print(answer)

# If you want to use both ' and " quote inside a string, then use triple-singe or triple-double quotes.
answer = '''I'm fine, doing "great".'''
print(answer)

answer = """I'm fine, doing "great"."""
print(answer)

# print(dir(answer)) # __iter__ present means strings are iterable
# indexing
text = "python"
print(text)
print(text[0]) # positive index. --> p
print(text[3]) # positive indexing --> h
print(text[-1]) # negative indexing  --> n
print(text[-2]) # negative indexing  --> o

# print(text[10])  #IndexError: string index out of range
# print(text[-10])   #IndexError: string index out of range

# string accessing
text = "python"
print("Manually")
print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5])

# using loops to access
print("using loops")
for char in text:
    print(char)


# len() -> Return the number of items in an object
text = "python"
print(len(text))
# print("Length is " len(text))  # SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("Length is ", len(text))

text = "python "
print("Length is", len(text)) # space is also a character

# example using list
list_data =["dell","lenovo","mac","acer"]
print("Brands Count is", len(list_data))

# len() -> doesn't work with numbers
# num =100
# print("Length is", len(num)) #TypeError: object of type 'int' has no len()

# Slicing In Python
text = "python"
print(text[0]) # access using index
print("----")

# [start:stop:step]
print(text[0:6:2]) # -->pto
print(text[0:3]) # start(0) : stop(3) --> pyt
print(text[2:5]) # start(2) : stop(5) --> tho
print(text[0:])  # start(0) : end  --> python
print(text[:])   # start : end  --> python
print(text[:3]) #  start : stop(3) --> pyt

print("------")
# Negative Slicing
text = "python"

        #  0   1  2  3  4  5 (positive indexing)
        #  p   y  t  h  o  n
        # -6  -5 -4 -3 -2 -1  (negative indexing)

print(text[-1])
print(text[-1:])
print(text[-4:-1]) # tho

print(text[-4:-1:1]) #tho
print(text[-4:-1:-1]) # empty
print(text[-4:-6:-1]) # ty

print(text[1:4:-1]) #empty

# Reversing String
print(text[::-1]) # end:start --> nohtyp 
 #same thing by logic
text = "python"
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text #adding each character to front
print("Reversed text:",reversed_text)


# Reassigning
text = "Hello"
print(text)

text = "Hi"
print(text)

# String Immutability
text = "Hello"
print(text)
# # modifying hello to Hello
# text[0]= "H"  # TypeError: 'str' object does not support item assignment
# print(text)

# String Concatenation
s1 = "Hello"
s2 = "Good Morning"
print(s1+s2)  # HelloGood Morning

age = 30
# print("My age is" + age) # TypeError: can only concatenate str (not "int") to str
print("My age is", age) # My age is 30
print("My age is", + age) # My age is 30
print("My age is" + str(age)) # My age is30 

# String Repetition 
text = "Ha"
laugh = "HaHaHaHa"
print(laugh)

laugh_hard = text * 10
print(laugh_hard)

# String Methods
text = "Ha"
print(dir(text))

# simulate gmail functionality using strings -> gmail.com
user_given_email = "Puja2Bharti"
format_email = user_given_email.lower() +"@gmail.com"
print("Gmail Auto Format ID: "+ format_email)

# simulate PAN creation  -> https://www.pan.utiitsl.com/panonline_ipg/forms/csfPan.html/csfPreForm
