#2Q.Write a python program to check whether a number is palindrome or not?
my_str = input('Enter a string in lowercase: ')

rev_str = ''

for char in my_str:
    rev_str = char + rev_str

if my_str == rev_str:
    print(f'{my_str} is a palindrome string')
else:
    print(f'{my_str} is not a palindrome string')
