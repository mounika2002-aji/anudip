#5.Generating a number between a range
import random
lower_value=int(input('Enter the lower value of range:'))
upper_value=int(input('Enter the upper value of range:'))
random_number=random.randint(lower_value,upper_value)
print(f'random number between{lower_value}and{upper_value}')
print(f'A random number between {lower_value}and{upper_value}')
