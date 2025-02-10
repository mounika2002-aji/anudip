while True:
    num1 = input("Enter number 1: ")
    if not num1.isdigit():
        print("Error: You can only enter numbers.")
        continue
        
    num2 = input("Enter number 2: ")
    if not num2.isdigit():
        print("Error: You can only enter numbers.")
        continue

    chose = input("Choose function a,m,d,s,M or 'q' to quit: ")
 
    if chose == 'q':
        print("Hope You Find Your Answers")
        break

    a = int(num1) + int(num2)
    m = int(num1) * int(num2)
    s = int(num1) - int(num2)

    if chose == 'd':
        if int(num2) != 0:
            d = int(num1) / int(num2)
            print(d)
        else:
            print("Error: You cannot divide a number by zero.")
    elif chose == 'M':
        if int(num2) != 0:
            print(int(num1) % int(num2))
        else:
            print("Error: You cannot perform modulus by zero.")
    elif chose == 'a':
        print(a)
    elif chose == 'm':
        print(m)
    elif chose == 's':
        print(s)
    else:
        print("Invalid function")
