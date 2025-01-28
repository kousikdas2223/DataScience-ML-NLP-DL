import numpy as np

arr1 = np.array([1,2,3,4,5])
print(arr1)
print(type(arr1))
print(arr1.shape)
print(arr1.flatten())

arr2 = np.array([10,20,30,40,50])
arr2.reshape(1,5)
print(arr2)
print(np.array([11,21,31,41,51]).reshape(1,5))
      
arr3 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr3)
print(arr3.shape)

arr4 = np.arange(0,10,2).reshape(1,5)
print(arr4)
print(np.ones((4,5)))

arr5 = np.zeros((3,4))
arr6 = np.eye(3)
print(arr5)
print(arr6)

# Numpy vectorized operations

arr7 = np.array([1,2,3,4,5])
arr8 = np.array([6,7,8,9,10])
print(arr7 + arr8)
print(arr7 - arr8)
print(arr7 * 2 + arr8)

# Universal Functions

arr9 = np.array([1,2,3,4,5])
print(np.sqrt(arr9))
print(np.exp(arr9))
print(np.log(arr9))
print(np.sin(arr9))
print(np.cos(arr9))
print(np.tan(arr9))

# Array slicing and indexing functions

arr10 = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr10[2:5])
print(arr10[::2])
print(arr10[::-1])
print(arr10[[1,3,5]])

arr11 = np.array([[1,2,3,4,5],[6,7,8,9,10],[10,11,12,13,14]])
print(arr11)
print(arr11[1,2])
print(arr11[2:, 3:])
print(arr11[:2, 3:])
print(arr11[0:3, 2:4])

# Statistical concepts -- Normalization
# to have mean of 0 and standard deviation of 2

arr12 = np.array([28,29,30,31,32,34])
mean = np.mean(arr12)
std_dev = np.std(arr12)
normalized_arr = (arr12 - mean) / std_dev
print(normalized_arr)

print(np.mean(arr12))
print(np.std(arr12))
print(np.median(arr12))
print(np.var(arr12))





