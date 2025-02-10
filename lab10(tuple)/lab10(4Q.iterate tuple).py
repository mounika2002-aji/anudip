#4Q.Write a python program and iterate the given tuples 

#Input: 

employee1 = ("John Doe", 101, "Human Resources", 60000) 

employee2 = ("Alice Smith", 102, "Marketing", 55000) 

employee3 = ("Bob Johnson", 103, "Engineering", 75000)

# Input tuples
employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)

# List of employee tuples
employees = [employee1, employee2, employee3]

# Iterate through the tuples and print details
for employee in employees:
    name, id, department, salary = employee
    print(f"Name: {name}, ID: {id}, Department: {department}, Salary: {salary}")
