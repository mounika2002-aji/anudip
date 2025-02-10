#4Q.write a python programe prompts the user to input two numbers and raise a TypeError exception if the input are not found numerical.
def get_number_input(prompt):
    user_input = input(prompt)
    if not user_input.isdigit():
        raise TypeError("Invalid input! Please enter a numerical value.")
    return int(user_input)

try:
    num1 = get_number_input("Please enter the first number: ")
    num2 = get_number_input("Please enter the second number: ")
    print(f"You entered the numbers: {num1} and {num2}")
except TypeError as e:
    print(e)
