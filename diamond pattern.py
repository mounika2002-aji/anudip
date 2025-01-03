#Q17.print the diomond patterns for rows = 5
rows = 5
for row in range(1, rows + 1):
    print(" " * (rows - row) + "*" * (2 * row - 1))

for row in range(rows - 1, 0, -1):
    print(" " * (rows - row) + "*" * (2 * row - 1))
