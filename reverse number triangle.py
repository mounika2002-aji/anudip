#Q19.print the Reverse Number Triangle for rows = 5
rows = 5
for row in range(rows, 0, -1):
    for col in range(1, row + 1):
        print(col, end=" ")
    print()
