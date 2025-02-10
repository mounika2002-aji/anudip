#4Q.Write a Python program to count and display the vowels of a given text 

String=”Welcome to python Training”

# Given string
String = "Welcome to python Training"

# Convert the string to lowercase to make it case-insensitive
String = String.lower()

# Initialize a dictionary to count vowels
vowel_count = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

# Loop through each character in the string
for char in String:
    if char in vowel_count:
        vowel_count[char] += 1

# Display the count of each vowel
print("Vowel counts:")
for vowel, count in vowel_count.items():
    if count > 0:
        print(f"{vowel}: {count}")
