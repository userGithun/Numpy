

# import numpy as np

# arr = np.array([1,2,3,4,5,6])
# #number of array
# newarr = np.array_split(arr,3)

# print(newarr)
# print()
# print(type(newarr))
# print(newarr[0])
# print(newarr[1])
# print(newarr[2])

#Spliting 2-D Arrays

# import numpy as np

# arr = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])

# newarr= np.array_split(arr,3)

# print(newarr)

import numpy as np

# arr = np.array([[1,2],[3,4],[5,6]])
arr= np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])

# newarr=np.array_split(arr,3, axis=1)
newarr= np.hsplit(arr,3)


print(newarr)