# import numpy as np

# arr= np.array([[1,2,3,4,5],[5,6,7,8,5]])

# print(arr.shape)
#(2,5) which enas the array has 2 dimensions and it has 4 element


import numpy as np

arr = np.array([1,2,3,4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)   