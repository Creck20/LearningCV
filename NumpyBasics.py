import numpy as np

#One way to initialize an array is using a Python sequence, such as a list. For example:
a = np.array([1, 2, 3, 4, 5, 6])
print(a)

#Two- and higher-dimensional arrays can be initialized from nested Python sequences:
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b)

"""
In NumPy, a dimension of an array is sometimes referred to as an “axis”. This terminology 
may be useful to disambiguate between the dimensionality of an array and the dimensionality 
of the data represented by the array. For instance, the array a could represent three points, 
each lying within a four-dimensional space, but a has only two “axes”.
"""

#an element of the array can be accessed by specifying the index along each axis within a single set of
#square brackets separated by commas.
print(f'Element in second row third column of b = {b[1, 2]}')  # Accessing the element in the second row, third column

#The shape of an array is a tuple of integers giving the size of the array along each axis.
print(f'Shape of b = {b.shape}')  # Output: (3, 3) since b is a 3x3 array

#the number of axes (or dimensions) of an array is given by its rank.
print(f'Rank of b = {b.ndim}')  # Output: 2 since b is a 2D array

#The total number of elements in an array is given by its size.
print(f'Size of b = {b.size}')  # Output: 9 since b has 3 rows and 3 columns    

#The data type of the elements in an array is given by its dtype.
print(f'Data type of elements in b = {b.dtype}')  # Output: int64 or int32 depending on the system

#You can also create arrays filled with zeros, ones, or a constant value using the following functions:
c = np.zeros((2, 3))  # Create a 2x3 array filled with zeros
print(f'Array c filled with zeros:\n{c}')

d = np.ones((2, 3))  # Create a 2x3 array filled with ones
print(f'Array d filled with ones:\n{d}')

e = np.full((2, 3), 7)  # Create a 2x3 array filled with the constant value 7
print(f'Array e filled with sevens:\n{e}')

#You can also create an identity matrix using the eye function:
f = np.eye(3)  # Create a 3x3 identity matrix
print(f'Identity matrix f:\n{f}')