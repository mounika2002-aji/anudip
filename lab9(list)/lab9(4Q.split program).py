#4Q.Write a Python program to split a given list into two parts where the length of the first part of the list is given. 

#Original list: [1, 1, 2, 3, 4, 4, 5, 1] 

#Length of the first part of the list: 3 

#Splitted the said list into two parts: ([1, 1, 2], [3, 4, 4, 5, 1])

def split_list(input_list, first_part_length):
    first_part = input_list[:first_part_length]
    second_part = input_list[first_part_length:]
    return first_part, second_part

# Original list
original_list = [1, 1, 2, 3, 4, 4, 5, 1]
# Length of the first part of the list
first_part_length = 3

# Split the list
first_part, second_part = split_list(original_list, first_part_length)

# Display the result
print(f"Splitted the said list into two parts: ({first_part}, {second_part})")
