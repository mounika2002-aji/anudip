#4Q.Python program to get the Fibonacci series between 0 to 50

# Function to generate Fibonacci series between 0 and 50
def fibonacci_series():
    fib_list = []
    a, b = 0, 1
    while a <= 50:
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

# Get the Fibonacci series between 0 and 50
fib_numbers = fibonacci_series()

# Print the Fibonacci series
print("Fibonacci series between 0 and 50:")
print(fib_numbers)
