#1Q.Write a Python program to find the number of times 4 appears in the tuple. 

#Input: 

#tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7 )

def count_occurrences(input_tuple, value):
    count = 0
    for item in input_tuple:
        if item == value:
            count += 1
    return count

# Input tuple
tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7)
# Count occurrences of the number 4
occurrences_of_4 = count_occurrences(tuplex, 4)

# Display the result
print(f"The number of times 4 appears in the tuple is: {occurrences_of_4}")
