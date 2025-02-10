#1Q.Write a Python program to sum all the items in a list.
def sum_list(items):
    total = 0
    for item in items:
        total += item
    return total

# Example usage
my_list = [1, 2, 3, 4, 5]
total_sum = sum_list(my_list)

# Display the result
print(f"The sum of all the items in the list is: {total_sum}")
