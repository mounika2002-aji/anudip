Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# +, -, *, /, is, in not in
# operator --> a person who operates a machine
# Arithmetic op --> +, -, *, /, %, **, //
# Comparision op --> these are the operators that we use to compare two operands
# 1. Operator
# 2. Operand
2 + 3
5
# operator performs an operation on operands
# Comparision op --> (<, >, <=, >=, ==, !=)
4 < 6
True
5 > 7
False
5 <= 5
True
7 > 7
False
# the answer of any comparision operator will always be boolean value (True, False)
6 == 9
False
7 != 4
True
a = 5
b = 7
a < b
True
b > a
True
a == b
False
a != a
False
'i' > 'n'
False
'C' > 'c'
False
# every char has an ascii value
ord('C')
67
ord('c')
99
ord('A')
65
ord('a')
97
# ABCD......Z, a, b, c, ......z
# 65, 66, 67, 68, 59.....
ord('z')
122
# 65.....122
26 + 26
52
122 - 65
57
ord('Z')
90
ord('[')
91
ord('\')
    
SyntaxError: unterminated string literal (detected at line 1); perhaps you escaped the end quote?
ord('\\')
    
92
# A, B, C, ......, Z, [, \, ], ^, _, `, a, b, c, .......z
    
52 + 6
    
58
122 - 65 + 1
    
58
# ASCCI values of any char --> ord()
    
# ASCII values of any char --> ord()
    
'[' < 'a'  # 91 < 97
       
True
True > False  # True --> 1, False --> 0
    
True
False > True
    
False
# char --> ASCII --> ord()
    
# ASCII --> char --> chr()
    
chr('A')
    
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    chr('A')
TypeError: 'str' object cannot be interpreted as an integer
chr(
    )
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    chr(
TypeError: chr() takes exactly one argument (0 given)
chr(65)
'A'
chr(97)
'a'
chr(90)
'Z'
# ASCII --> CHAR --> chr()
# CHAR --> ASCII --> ord()
True != false  #
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    True != false  #
NameError: name 'false' is not defined. Did you mean: 'False'?
True
True
False
False
# true, false
True != False
True
# Assignment operators --> We use thes opearator to assign a value to a variable
# =, +=, -+, *=, /=, %=, **=, //=
# =, +=, -=, *=, /=, %=, **=, //=
first_name = 'Alice'
# we are assiging a value('Alice') a variable(first_name) by using '= '(assignment operator)
a = 5
b = 6
c = a * b
c
30
a
5
a += 2  # a = a + 2
a
7
b -= 1  # b = b - 1
b
5
c -= (a += b)
SyntaxError: invalid syntax
c -= a + b
c
18
# c = c - (a + b)
# ++, -- <-- python does not have these operators
a *= (c - b)  # a = a * (c - b)
a
91
# Logical Operators --> we use these operators to compare the multiple comparisions
# when we want to use boolean logic we will use it
# AND, OR, NOT
# when both the conditions are True then AND will be True
# T AND T --> T
# T AND F --> F
# F AND T --> F
# F AND F --> F
4 < 7 and 8 != 4    # T AND T  --> T
True
True != False and 'X' > 'z'  # T AND F --> F
False
c
18
c == False and True   #  F AND T --> F
False
c == a and False >= 5  # F AND F --> F
False
# OR
# T OR T --> T
# T OR F --> T
# F OR T --> T
# F OR F --> F
4 < 7 or 8 != 4    # T OR T  --> T
True
True != False or 'X' > 'z'  # T OR F --> T
True
c == False or True   #  F OR T --> T
True
c == a or False >= 5  # F OR F --> F
False
>>> # NOT
>>> # T NOT --> F
>>> # F NOT --> T
>>> not True
False
>>> not False
True
>>> not (4 > 6)
True
>>> not (True == False)
True
>>> not 6 > 3
False
>>> not True <= 1  # not T --> F,   not True --> 0 <= 1 --> t
False
>>> # precedence of comparision and logical operators
>>> '''
... Comparisons (<, <=, >, >=, ==, !=)
... not
... and
... or
... '''
'\nComparisons (<, <=, >, >=, ==, !=)\nnot\nand\nor\n'
>>> x = 5
>>> y = 10
>>> z = 15
>>> x < y and not y > z or x == z  # T
True
>>> x >= y and z == True or not False and 5 > 8 and not z > y or 8  # T
8
