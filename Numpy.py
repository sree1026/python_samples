import numpy as np
import time
import sys

num = np.array([(1,2,3),(4,5,6),(7,6,9)])
print(num.shape)
print(num.ndim)
print(num.dtype)
print("\n\n"+str(num))
print("Sum of rows: "+str(num.sum(axis=0)))
print("Sum of columns: "+str(num.sum(axis=0)))


