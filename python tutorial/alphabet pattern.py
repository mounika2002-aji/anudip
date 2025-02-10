#Q21.print the Alphabet Pattern for rows = 5
rows = 5
for row in range(1, rows + 1):
    for col in range(1, row + 1):
        print(chr(64 + col), end=" ")
    print()  
