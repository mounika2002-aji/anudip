#5.write a programme to find the hypotenus of a triangle from it's side
import math
#input of the two triangle
side1=float(input("Enter the length of the first side:"))
side2=float(input("Enter the length of the secondside:"))
hypotenuse=math.sqrt(side1**2+side2**2)
print(f"The hypotenuse of the triangle is:{hypotenuse:.2f}")
