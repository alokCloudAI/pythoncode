# basic opr on array

# Arithmatic op on array aelemntwise
import numpy as np

a = np.array([10,20,30,4])
b = np.array ([5,10,15,20])
print(a + b)
print("***********")
print(a-b)
print("***********")
print(a*b)
print("***********")
print(a/b)
print("***********")
print(a//b)
print("***********")
print(a.sum())
print("***********")
print(a.min())
print("***********")
print(a.max())
print("***********")
print(a.sum(axis=0))

val = np.array([10,20,30,4])
print("***********")

print(val.mean())

print("***********")

print(np.median(val))
