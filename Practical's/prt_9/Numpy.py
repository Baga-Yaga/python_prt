import numpy as np
# print(np.__version__)
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
arr_2d = np.array([[1,2,3,4,5], [6,7,8,9,10]])
arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr1 = arr.reshape(3,2,2)
print(arr1)

print("Element of 2d-arr: ",arr_2d[1,3])
print("Slicing :",arr_2d[1, 1:4])
print("Slicing :",arr_3d[0:2, 2])
print("Slicing :",arr[0:2, 1:4])
print("Element of 3d-arr",arr_3d[0, 1, 2])
print("Shape :", arr_2d.shape)