#Q4.Python program to find the area of a triangle whose sides are given
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

s = (a + b + c) / 2

area = (s * (s - a) * (s - b) * (s - c)) ** 0.

print("The area of the triangle is:", area)
