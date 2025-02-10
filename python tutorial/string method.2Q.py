#2Q.Write a Python program to remove duplicate characters of a given string. 

Input = “String and String Function” 

Output: String and Function

input_str = "String and String Function"
words = input_str.split()

output_str = ' '.join([''.join(sorted(set(word), key=word.index)) for word in words])

print(output_str)
