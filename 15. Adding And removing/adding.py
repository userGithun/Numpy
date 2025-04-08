import numpy as np

a=np.array([[20,40],[60,80]])
# a = np.array([[20,40],[60,80]])
# print(np.append(a,[90,80]))
# print(np.insert(a,1,50))#Array index value
# print(np.insert(a,1,[50,60],axis=1))
# print(np.delete(a,1))
print(np.delete(a,1,axis=0))