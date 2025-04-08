

# import numpy as np

# arr = np.array([1,2,3])

# for x in arr :
#     print(x)


# #Iterating 2-D arrays

# import numpy as np

# arr = np.array([[1,2,3],[4,5,6]])

# for x in arr:
#     print(x)
#     print(type(x))


# #Iterating on each scaler element of the 2-D array

# import numpy as np

# arr=np.array([[1,2,3],[4,5,6]]) #index ke ander index

# for x in arr:
#     for y in x:
#         print(y)


#Itrating 3-D arrays
# import numpy as np

# arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

# for x in arr:
#     for y in x:
#         for z in y:
#             print(z)

# #Iterating arrays using nditer()

# import numpy as np

# # arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# # arr = np.array([[1,2,3],[4,5,6]])
# # arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

# for x in np.nditer(arr):
#     print(x)

# import numpy as np
# arr=np.array([[1,2,3,4],[5,6,7,8]])

# for x in np.nditer(arr[:,::2]):
#     print(x)