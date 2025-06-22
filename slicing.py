#Accessing and slicing 
import numpy as np 

arr1 = np.array([[1,2,3,4],
                 [5,6,7,8],
                 [-8,-7,-6,-5],
                 [-4,-3,-2,-1]])

print("Array 4:",arr1)
print("Array4 values of 1st and 2nd row are:\n",arr1[1:3,:])
print("Array4 values of 1st two rows and colums 0 and 2: \n",arr1[:2,::2])