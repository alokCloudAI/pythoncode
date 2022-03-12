import numpy as np
lst = [[1,2,3,'abc'], [3,6,9,12]]

a = np.array(lst)
print(a.ndim)
print("===================================")
print(a)
print("===================================")
print(a.size)
print("===================================")
print(a.shape)
dir(np)