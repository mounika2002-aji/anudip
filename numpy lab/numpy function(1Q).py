#1.suppose you have a dataset containing daily temperature reading for city, and you want to identify days with extreme temperature conditions.Find days where the temperature either exceeded 35 degree Celsius (hit day) or dropped below 5 degrees Celsius (cold day).
#input:
#temperature = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8,37.2])

import numpy as np
# Temperature data
temperature = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])

# Identify hot days (temperature > 35) or cold days (temperature < 5)
hot_days = temperature > 35
cold_days = temperature < 5

# Combine both hot and cold days conditions
extreme_days = hot_days | cold_days

# Get the indices of the extreme days
extreme_day_indices = np.where(extreme_days)[0]

# Output the extreme temperature days (either hot or cold)
print("Extreme Temperature Days (either > 35°C or < 5°C):")
for index in extreme_day_indices:
    print(f"Day {index+1}: {temperature[index]}°C")
