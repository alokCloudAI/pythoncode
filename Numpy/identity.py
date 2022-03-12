# identity matrix

# n * n

# diagonal is 1
import numpy as np 

print(np.random.randint(4,10 , (4,5)))
print("====================")
print(np.eye(5))
print("====================")
print(np.random.rand(4,5))
print("======Change the shape of Array=======")
a = np.arange(6)
print(a)

# transpose of an array (matrix)

# a = m * n
# b = n * m
print("transpose of an array (matrix)")
a2 = np.arange(18).reshape(6,-1)
print(a2)