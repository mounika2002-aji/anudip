#Q22.print the Floyd’s Triangle pattern for rows = 5
rows = 5
num = 1

for row in range(1, rows + 1):
    for col in range(1, row + 1):
        print(num, end=" ")
        num += 1
    print()  
