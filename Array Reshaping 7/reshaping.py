# import numpy as np

# arr = np.array([1,2,3,4,5,6,  7,8,9,10,11,12])

# # newarr = arr.reshape(4,3)
# newarr = arr.reshape(2,3,2)  #Convert the following 1-D array with 12 elements into 3-D array.

# print(newarr)

# import numpy as np
# arr =np.array([1,2,3,4,5,6,7,8])

# newarr=arr.reshape(3,3)

# print(newarr)

#return copy or Views?
# import numpy as np

# arr = np.array([1,2,3,4,5,6,7,8])

# print(arr.reshape(2,4).base)#view hai view original doc ko show karta hai ## copy hota to shape mai aata

#Unkown Dimension

# import numpy as np
# arr = np.array({1,2,3,4,5,6,7,8})

# newarr=arr.reshape(2,2,-1) #-1 Unknown Dimension (2)

# print(newarr)

#Flatting the arrays 1-D
import numpy as np

arr = np.array([[1,2,3],[4,5,6]])

newarr=arr.reshape(-1)

print(newarr)

