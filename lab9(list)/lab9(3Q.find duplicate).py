#3Q.Write a Python program to find duplicate values from a list and display those.
def find_duplicates(input_list):
    duplicates = []
    seen = set()
    for item in input_list:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        seen.add(item)
    return duplicates

# Example usage
my_list = [1, 2, 3, 4, 5, 3, 2, 1, 6, 7, 8, 9, 9]
duplicates = find_duplicates(my_list)

# Display the result
print(f"Duplicate values are: {duplicates}")

