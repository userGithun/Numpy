import numpy as np

a=np.array(42)
b=np.array([1,2,3,4,5])
c=np.array([[1,2,3,],[4,5,6]])
d=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#creating an array with 5 dimension and verify that it has 5 dimensions:
#1-D ko 5 dimensions

import numpy as np

arr = np.array([1,2,3,4], ndmin=6)

print(arr)
print('number of dimension :', arr.ndim)