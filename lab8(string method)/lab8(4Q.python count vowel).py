#4Q.Write a Python Count vowels in a string 

#input= “Welcome to Python Assignment” 

#Output: Total vowels are: 8
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

# Input
input_string = "Welcome to Python Assignment"
# Count vowels
vowel_count = count_vowels(input_string)

# Display the result
print(f"Total vowels are: {vowel_count}")
