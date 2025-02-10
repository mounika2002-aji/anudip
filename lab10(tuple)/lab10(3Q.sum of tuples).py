#3Q.Write a Python program to calculate the sum of the numbers in a given tuple.

# Input:

#tuples_list = [(1, 2), (3, 4), (5, 6)]

def sum_of_tuples(tuples_list):
    total_sum = 0
    for tpl in tuples_list:
        total_sum += sum(tpl)
    return total_sum

# Input list of tuples
tuples_list = [(1, 2), (3, 4), (5, 6)]
# Calculate the sum of the numbers in the tuples
total_sum = sum_of_tuples(tuples_list)

# Display the result
print(f"The total sum of the numbers in the given tuple is: {total_sum}")
