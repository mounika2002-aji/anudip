#lab Q1. Declare a div() function with two parameters. Then call the function and pass two
# numbers and display their division.

def div(num1, num2):
    '''This function returns num1/num2, where num2 is not zero'''  # doc string
    if num2 != 0:
        return round(num1 / num2, 2)
    return 'Can not divide by zero'
