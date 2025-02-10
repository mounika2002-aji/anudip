#2Q.Write a Python program to convert a list to a tuple.

#Input:

#listx = [5, 10, 7, 4, 15, 3]

def list_to_tuple(input_list):
    return tuple(input_list)

# Input list
listx = [5, 10, 7, 4, 15, 3]
# Convert the list to a tuple
tuplex = list_to_tuple(listx)

# Display the result
print(f"The converted tuple is: {tuplex}")
