#Q2.Write a NumPy program to create a 3*3 matrix with values ranging from 2 to 10.?

#sample Output: [2 3 4 ]
               #[5 6 7]
               #[8 9 10].

import numpy as np
# Create an array of values ranging from 2 to 10
matrix = np.arange(2, 11).reshape(3, 3)
print(matrix)

