#2Q.Write a Python program to remove a newline in Python 

String = "\nBest \nDeeptech \nPython \nTraining\n"

# Remove newline characters using the strip() method
cleaned_string = String.replace("\n", " ")

# Print the cleaned string
print("String without newline characters:")
print(cleaned_string)
