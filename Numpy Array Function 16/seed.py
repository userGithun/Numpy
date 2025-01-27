import numpy as np

np.random.seed(20)
mat=np.random.randint(1,21,9).reshape(3,3)

print(mat)
# mat1 = np.sum(mat)
# mat1 = np.min(mat)
# mat1 = np.max(mat)
# mat1 = np.max(mat,axis=0) #1 row
# mat1 = np.sum(mat,axis=0)
mat1 = np.cumsum(mat)     #axis=1

print(mat1)