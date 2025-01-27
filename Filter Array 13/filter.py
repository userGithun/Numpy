import numpy as np
#creating

# arr= np.array([41,42,43,44])

# x=[True,False,True,False]

# newarr= arr[x]

# print(newarr)

import numpy as np

# arr = np.array([41,42,43,44])
# #create an each element in arr

# filter_arr=[]
# #go through each element in arr

# for element in arr:
#     #if element is higherr than 42 , set the value to true,otherwise false:
#     if element > 42:
#         filter_arr.append(True)
#     else:
#         filter_arr.append(False)

# newarr =arr[filter_arr]
# print(newarr)            

#creating Filter directly from Array
import numpy as np

# arr =np.array([41,42,43,44])

# filter_arr = arr > 42

# newarr = arr[filter_arr]

# print(filter_arr)
# print(newarr)

import numpy as np

# arr = np.array([1,2,3,4,5,6,7])

# filter_arr =arr%2 ==0

# newarr=arr[filter_arr]

# print(newarr)
# print(filter_arr)


##1

import numpy as np

n = input("Enter name for verification\n")

filter_arr = n == 'pninfosys'

newarr = n[filter_arr]

print(f"Verification is : ",filter_arr)
