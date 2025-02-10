#4.write a programme calculating area of circle
#Input the radius
import math
radius =float(input("Enter the radius of the circle:"))
area=math.pi*radius **2
print(f"The area of the circle with radius {radius}is:{area:.2f}")


#5.write a programme to find the hypotenus of a triangle from it's side
import math
#input of the two triangle
side1=float(input("Enter the length of the first side:"))
side2=float(input("Enter the length of the secondside:"))
hypotenuse=math.sqrt(side1**2+side2**2)
print(f"The hypotenuse of the triangle is:{hypotenuse:.2f}")
