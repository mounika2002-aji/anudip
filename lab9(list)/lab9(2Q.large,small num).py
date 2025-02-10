#2Q.Write a Python program to get the largest and smallest number from a list without builtin functions.

def find_largest_smallest(numbers):
    if not numbers:  # Check if the list is empty
        return None, None
    
    largest = numbers[0]
    smallest = numbers[0]
    
    for num in numbers[1:]:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    
    return largest, smallest

# Example usage
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
largest, smallest = find_largest_smallest(my_list)

# Display the result
print(f"The largest number in the list is: {largest}")
print(f"The smallest number in the list is: {smallest}")
