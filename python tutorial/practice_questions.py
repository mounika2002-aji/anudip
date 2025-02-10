# Q1. Write a program to convert kilometers to miles

##kilometers = float(input('Enter the distance in km: '))
##
### 1 km = 0.621371 miles
##
##conversion_factor = 0.621371
##
##miles = kilometers * conversion_factor
##
##print(f'{kilometers} km in miles is = {miles:.2f}')


# Q2. Swap two variable values using third variable

##cup1 = 'cofee'
##cup2 = 'tea'
##
##print(f'Initial content cup1 = {cup1}, cup2 = {cup2}')
##
### answer --> cup1 = 'tea', cup2 = 'cofee'
##
##cup3 = cup1  # cup3 = cofee, cup1 = empty
##cup1 = cup2  # cup1 = tea, cup2 = empty
##cup2 = cup3  # cup2 = cofee, cup3 = empty
##
##print(f'After sawp content cup1 = {cup1}, cup2 = {cup2}')


# Q3. Swap two variable values without using third variable

# inplace swaping

##cup1, cup2 = cup2, cup1
##
##print(f'After sawp content cup1 = {cup1}, cup2 = {cup2}')
##
##
##num1 = 5
##num2 = 7
##
##num1, num2 = num2, num1
##
##print(f'After sawp content num1 = {num1}, num2 = {num2}')


# Q4. write a program to calculate the area of circle

##import math

##radius = float(input('Enter the length of radius: '))
##
### area_of_circle = 3.14 * radius ** 2
##
##area_of_circle = math.pi * radius ** 2
##
##print(f'Area of circle with radius {radius} = {area_of_circle:.2f}')


# Q5. write a program to find the hypotenus of a triangle from it's sides

# (hy)^2 = (side1)^2 + (side2)^2

# c = sqrt(a^2 + b^2)

##side1 = float(input('Enter the lenght of side1: '))
##side2 = float(input('Enter the lenght of side2: '))
##
##hypo = math.sqrt(side1 ** 2 + side2 ** 2)
##
##print(f'The hypotenus of triangle with sides {side1} and {side2} = {hypo:.2f}')


# Q5. Generate a random number between a range

##import random
##
##lower_value = int(input('Enter the lower values of range: '))
##
##upper_value = int(input('Enter the upper values of range: '))
##
##random_number = random.randint(lower_value, upper_value)
##
##print(f'A random number between {lower_value} and {upper_value} is {random_number}')


# Q6. Write a python program to convert celsius to fahrenheit

##celsius = float(input('Enter temperature in celsius: '))
##
##fahreheit = (celsius * (9/5)) + 32
##
##print(f'{celsius} degress is eqaul to {fahreheit} degree fahreheit')


# Q7. Display the month of calender for a certain year

##import calendar
##
##year = int(input('Enter a year: '))
##month = int(input('Enter a month: '))
##
##cal = calendar.month(year, month)
##print(f'The calender for {month}/{year}:')
##print(cal)




















