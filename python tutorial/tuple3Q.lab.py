#3Q.Write a Python program to calculate the sum of the numbers in a given tuple.
# Input:

tuples_list = [(1, 2), (3, 4), (5, 6)]

total_sum = sum(sum(tup) for tup in tuples_list)

print("The sum of the numbers in the given tuple list is:",total_sum)


