#2Q.write a python programe that prompts user to input integer and raise a ValueError exception if the input is not a valid integer.

def get_integer_input():
    try:
        user_input = input("Please enter an integer: ")
        user_int = int(user_input)
        print(f"You entered the integer: {user_int}")
    except ValueError:
        raise ValueError("Invalid input! Please enter a valid integer.")

# Example usage
try:
    get_integer_input()
except ValueError as e:
    print(e)
