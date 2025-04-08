#Now we will create a numpy ndarray object
#the array object in numpy is call ndarray
#array()
import numpy as np
# x=np.array([1,2,3,4,5])
# print(x)
# print(type(x))

#we can also pass a list , tuple or any array link object with array().and it
#will be converted to ndarray

# y=np.array((1,2,3,4,5))
# print(y)
# print(type(y))


#Dimensions in Array
#A dimension in array is one level of array depth (nested arrays).

# 0 - Dimensions Array :-
# 0 - D Array, or Scalars, are the elements in an array.each value in an array is 0-D array.

arr = np.array(42)

print(arr)  #0 - D ka khud ka ek element hota hai


#2 - D Array :-
#create a 2-D array containing 2 Arrays with certain
import numpy as pn

arr = np.array([[1,2,3],[4,5,6]])
#1 2 3
#4 5 6

print(arr)
print("Dismension of Array",arr.ndim)
print("Shape of Array=",arr.shape)

#3-D Arrays :-
#Now we will create a 3-D array with two 2-D array
import numpy as np

arr=np.array([[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]])

print(arr)
print('shape of array=',arr.shape)
print('Dimension of array',arr.ndim)