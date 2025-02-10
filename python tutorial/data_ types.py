#Data types in python
# Data types is a certain type data that we store in a variable
# numeric, text, boolean, collections, binary

# 1. Numeric Data Types:

# a. int(integer)
# int is a whole number
# range : (-inf to +inf)
# eg. 0, -65, 3, -567, 345

num1 = 4
num2 = -8
num3 = 0

# to check the data type of a varible use type() function 


# Alt + 3 --> comment the selected code
# Alt + 4 --> Uncomment the selected code

print(type(num1))
print(type(num2))
print(type(num3))


# b. float
# float is a decimal number
# range: (-inf to +inf)
# eg. -7.34, 3.14, 1.273, -0.00000012

##num4 = -7.34
##num5 = 3.14
##num6 = -0.00000012
##
##
##print(type(num4))
##print(type(num5))
##print(type(num6))


# c. complex
# complex number is a combination of real number and imaginary number
# sqrt(-1) --> does not exist
# sqrt(-1) --> iota
# eg. (2 + 3j), (-5.87j), (-2.98 - 5.24j)

# (2 + 3j)
# real number --> 2
# imaginary num --> 3j

# (-5.87j)
# real number --> 0
# imaginary num --> -5.87j


# (-2.98 - 5.24j)
# real number --> -2.98
# imaginary num --> -5.24j

##num7 = (2 + 3j)
##num8 = (-5.87j)
##num9 = (-2.98 - 5.24j)


##print(type(num7))
##print(type(num8))
##print(type(num9))

# real and imaginary part of num7
##print(num7.real)
##print(num7.imag)


# real and imaginary part of num8
##print(num8.real)
##print(num8.imag)


# real and imaginary part of num9
##print(num9.real)
##print(num9.imag)



# 2. String Data type
# It is a textual data type which contains the text in the quotes
# eg. 'Python', "Alice Johnson", '''Anudip@123''', """Python classes 123"""

##str1 = 'Python'
##str2 = "This is a python code"
##str3 = '''This is
##        also a string, but
##        in multiple
##        line'''
##str4 = """This is
##        a python 
##        programmming
##        class"""
##
##print(str1)
##print(str2)
##print(str3)
##print(str4)
##
##
##print(type(str1))
##print(type(str2))
##print(type(str3))
##print(type(str4))


# multiline strings
# by using single and double quotes we can not write multiline string
# to write a multiline string use triple quotes (single/double)

# this will give an error
##x = "this
##is
##a multiline
##str"
##
##print(x)
##
##
##y = '''This is
##a multiline
##string example'''
##
##print(y)
##
##
##z = """Python
##Programming
##Class, this
##is a DAP
##Course"""
##
##print(z)
##
##print(type(y))
##print(type(z))




# 3. Boolean Data type
# this data type stores either True or False Values
# eg. True, False

##bool1 = True
##print(bool1)
##print(type(bool1))
##
##bool2 = False
##print(bool2)
##print(type(bool2))



# Type Casting:
# Converting one data type to other

# 1. float --> int
##int1 = int(23.54355)  # 23
##print(int1)

# 2. str --> int (str must only contain integers)
##int2 = int('123')
##print(int2)

##int2 = int('435.6787')  # it can not type cast 
##print(int2)

##int3 = int('123abc')  # it will give an error
##print(int3)


# 3. bool --> int

##int4 = int(True)  # 1
##print(int4)
##
##int5 = int(False)  # 0
##print(int5)







