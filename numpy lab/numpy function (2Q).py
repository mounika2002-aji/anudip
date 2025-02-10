#Q2.Suppose you have a dataset containing monthly sales data for a company,and you want
#to splint this data into quarterly reports for analysis and reporting purposes.


import numpy as np

monthly_sales = np.array([120, 135, 148, 165, 180, 155, 168, 190, 205, 198, 210, 225])

# Reshape the array into quarters
quarters = monthly_sales.reshape(-1, 3)

# Now, calculate the total sales for each quarter
quarterly_sales = quarters.sum(axis=1)

print("Quarterly Sales Report:")
print(quarterly_sales)
