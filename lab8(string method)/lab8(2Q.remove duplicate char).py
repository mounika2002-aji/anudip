#2Q.Write a Python program to remove duplicate characters of a given string. 

#Input = “String and String Function” 

#Output: String and Function 

# Function to remove duplicate characters from a given string
def remove_duplicates(input_string):
    seen_chars = set()
    result = []
    for char in input_string:
        if char not in seen_chars:
            seen_chars.add(char)
            result.append(char)
    return ''.join(result)

# Input
input_string = "String and String Function"
# Remove duplicate characters
output_string = remove_duplicates(input_string)

# Display the result
print(output_string)

