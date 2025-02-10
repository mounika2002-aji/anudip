#4Q.Suppose you have two sets of employee data-one containing information about full-time employees and another information about part-time employees.You want to combine this data to create a comprehensive employee dataset for HR analysis.
#Input:Employee data for full-time employees
#full_time_employees = np.array([
import numpy as np

# Full-time employees data
full_time_employees = np.array([
    [101, 'John Doe', 'Full-time', 55000],
    [102, 'Jane Smith', 'Full-time', 60000],
    [103, 'Mike Johnson', 'Full-time', 52000]
])

# Part-time employees data
part_time_employees = np.array([
    [201, 'Alice Brown', 'Part-time', 20000],
    [202, 'Bob White', 'Part-time', 22000],
    [203, 'Charlie Green', 'Part-time', 18000]
])

# Combine the datasets using np.concatenate
combined_employees = np.concatenate((full_time_employees, part_time_employees), axis=0)

# Display the combined dataset
print("Combined Employee Data:")
print(combined_employees)

# Perform analysis - Example: Count the total number of employees
total_employees = combined_employees.shape[0]
print(f"\nTotal number of employees: {total_employees}")
