#3Q.Suppose tou have a dataset containing customer data,and you want to split this data into two group for customers who made a purchase in the last days and another group for customers who haven't made in the last 30 days.
#input:customers_ids=np.array([101,102,103,104,105,106,107,108,109,110]) last_purchase_days_ago=np.array([5,15,20,25,30,35,40,45,50,55])


import numpy as np

# Customer data
customer_ids = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110])
last_purchase_days_ago = np.array([5, 15, 20, 25, 30, 35, 40, 45, 50, 55])

# Define the threshold for recent purchases (within the last 30 days)
recent_purchase_mask = last_purchase_days_ago <= 30

# Split the data based on the mask
recent_customers = customer_ids[recent_purchase_mask]
non_recent_customers = customer_ids[~recent_purchase_mask]

# Output the results
print("Customers who made a purchase in the last 30 days:")
print(recent_customers)

print("\nCustomers who haven't made a purchase in the last 30 days:")
print(non_recent_customers)
