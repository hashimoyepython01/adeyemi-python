# -*- coding: utf-8 -*-
"""checkyypoi4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nqmjfWFaDR_0bK9Fvb7Vfnf7X5eoUeQa
"""

#que1
import numpy as np


hash = np.array([1,2,3,4])
hash.tolist()
print(hash)

#que2
import numpy as np
hash=np.array([[1,2,3],[1,2,3],[2,3,4]])

                                             
y = np.trace(hash)

print(y)

#qu3
import numpy as np
hash=[1,2,3,4,5]
max=0
n=len(hash)
for i in range (1,n):
  if hash[i]>max:
    max=hash[i]
print("all the maximum number", max)

#que4
import numpy as np
aa=np.array([1,2,3,4])
bb=np.array([5,6,7,8])
c = aa+bb
print(c)

#que
matrix1=[[10,11,12],[13,14,15],[16,17,18]]
matrix2=[[1,2,3],[4,5,6],[7,8,9]]
rmatrix=[[0,0,0],[0,0,0],[0,0,0]]
for i in range (len(matrix1)):
    for j in range(len(rmatrix[0])):
        rmatrix [i][j]= matrix1[i][j] - matrix2[i][j]
for r in rmatrix:
  print(r)