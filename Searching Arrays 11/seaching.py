#Array function search sorting filter

# import numpy as np

# arr = np.array([1,2,3,4,5,4,4])
# #0 1 2 3 4

# x = np.where(arr == 4)

# print(x)

#Find the indexings where the values are even:

# import numpy as np

# arr = np.array([1,2,3,4,5,6,7,8])

# # x = np.where(arr%2 ==0)
# x = np.where(arr%2 ==1)

# print(x)

#Search Sorted
import numpy as np

arr = np.array([6,8,7,9])

x = np.searchsorted(arr,7)
#index number

print(x)