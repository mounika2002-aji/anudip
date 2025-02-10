#Q20.print the Number Pyramid for rows = 5
rows = 5
for row in range(1, rows + 1):

    print(" " * (rows - row), end = "")
    
    for col in range(1, row + 1):
        print(col, end = "")
    
    for col in range(row - 1, 0, -1):
        print(col, end = "")
    print()  
