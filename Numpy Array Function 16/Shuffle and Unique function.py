#Suffle and Unique
import numpy as np
# # arr= np.arange(10)
# # arr= np.array([1,2,3,4,5,6,3,2,])
# arr= np.arange(9).reshape((3,3))
# np.random.shuffle(arr)
# print(arr)


#Unique
arr= np.array([1,2,3,4,1,3,5])

x= np.unique(arr)
x= np.unique(arr).size
x= np.unique(arr,return_index=True,return_counts=True)

print(x)