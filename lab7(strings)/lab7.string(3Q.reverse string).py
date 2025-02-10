#3Q.Write a Python program to reverse words in a string 
String = "Deeptech Python Training"
# Given string
String = "Deeptech Python Training"

# Split the string into a list of words
words = String.split()

# Reverse the list of words and join them back into a string
reversed_string = " ".join(reversed(words))

# Print the reversed string
print("Reversed string:")
print(reversed_string)
