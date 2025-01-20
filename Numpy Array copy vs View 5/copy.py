#Make a copy, change the original array, and display both arrays:
import numpy as np
 
arr = np.array([1, 2, 3, 4, 5]) 
x = arr.copy()
arr[0]=42

print(arr)
print(x) #The copy SHOULD NOT be a affected by the changes made to the original array.


#VIEW: Make a view, change the original array, and display both arrays:

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0]=42

print(arr)
print(x) #The view SHOULD be affected by the changes made to the original array.