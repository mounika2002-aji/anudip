#4Q.Accept numbers using input() function until the user enters 0. If user input 0 then break the while loop and display the sum of all the numbers

# Function to calculate the sum of numbers until the user enters 0
def sum_numbers():
    total_sum = 0
    while True:
        # Accept user input
        num = int(input("Enter a number (0 to stop): "))
        
        # Break the loop if the user enters 0
        if num == 0:
            break
        
        # Add the number to the total sum
        total_sum += num
    
    return total_sum

# Call the function and display the result
result = sum_numbers()
print(f"The sum of all entered numbers is: {result}")
