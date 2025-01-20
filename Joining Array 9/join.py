# import numpy as np

# arr1 = np.array([1, 2, 3])

# arr2 = np.array([4, 5, 6])

# arr = np.concatenate((arr1 , arr2))

# print(arr)

#Join two 2-D arrays along rows (axis=1)

# import numpy as np

# arr1 = np.array([[1,2],[3,4]])

# arr2 = np.array([[5,6],[7,8]])
# #axis =1 row

# arr =np.concatenate((arr1,arr2),axis=1) #index 1 2 5 6 (0)

# print(arr)

#Joining Arrays using stack Functions
#new axis

# import numpy as np
# arr1 = np.array([1, 2, 3])

# arr2 = np.array([4, 5, 6])

# arr = np.stack((arr1 ,arr2),axis=1)#row col=0

# print(arr)

#stactking Along Rows : numPy provides a helper function: hstack

# import numpy as np
# arr1 = np.array([1, 2, 3])

# arr2 = np.array([4, 5, 6])

# arr = np.hstack((arr1 ,arr2))#row

# print(arr)

#numPy provides a helper function: vstack() to stack col


# import numpy as np
# arr1 = np.array([1, 2, 3])

# arr2 = np.array([4, 5, 6])

# arr = np.vstack((arr1 ,arr2))#col

# print(arr)


#stacking Along height (depth):Numpy provides a helper function:
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4 , 5, 6])

arr = np.dstack((arr1,arr2))#hight

print(arr)
