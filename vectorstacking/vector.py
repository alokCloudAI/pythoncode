import numpy as np
a = np.array([["New York","Maryland"],["Albany","Annapolis"]])

b = np.array([["Ohio","Arizona"],["Columbus","Phoenix"]])
print(a)
print(a.shape)
print("************************")
print(b)
print(b.shape)

print("************************")
print(np.concatenate((a,b) ,  axis = 0))

print("***********axis = 1 means column-wsie*************")

# axis = 1 means column-wsie
print(np.concatenate((a,b) ,  axis = 1))
print("***********Stack*************")

# stack

print(np.vstack((a, b)))