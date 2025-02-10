#5Q.Write a Python program to traverse a given list in reverse order, and print the elements with the original index. Original list: ['red', 'green', 'white', 'black'] 

#Traverse the said list in reverse order: 

#black 

#white 

#green

#red

def traverse_reverse(input_list):
    for i in range(len(input_list) - 1, -1, -1):
        print(f"{input_list[i]}")

# Original list
original_list = ['red', 'green', 'white', 'black']

# Traverse and print in reverse order
print("Traverse the said list in reverse order:")
traverse_reverse(original_list)
