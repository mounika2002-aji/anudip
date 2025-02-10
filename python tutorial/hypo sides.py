#Q5. write a program to find the hypotenus of a triangle from its sides

#(hy)^2 = (side1)^2 + (side2)^2

 #c = sqrt(a^2 + b^2)
import math
side1 = float(input('Enter the lenght of side1: '))
side2 = float(input('Enter the lenght of side2: '))

hypo = math.sqrt(side1 ** 2 + side2 ** 2)

print(f'The hypotenus of triangle with sides {side1} and {side2} = {hypo:.2f}')
