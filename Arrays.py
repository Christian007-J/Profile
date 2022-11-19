# Install numpy using the following command: pip install numpy
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 4, 7, 3, 15])
a = np.array([(1, 3, 4, 5), (4, 6, 7, 8), (3, 4, 5, 6)])
print(arr)
print(arr.ndim)
print(type(arr))

# indexing
print(arr[8])
print(a[1, 2])

# slicing
print(arr[1:9:2])
# getting data type of array elements
print(arr.dtype)

# copy and view

x = arr.copy()
arr[9] = 13
print(x)
print(arr)

y = arr.view()
arr[9] = 13
print(y)
print(arr)

# Array shape
print(arr.shape)
print(a.shape)

# Reshaping Array

newarr = arr.reshape(5, 3)
print(newarr)

# iterating

for i in arr:
    print(i)
# iterating in 2 D array
for x in a:
    for y in x:
        print(y)

# iterating in 3 D array
b = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in b:
    print(b)

# joining arrays
arr1 = np.array(["a", "b", "c"])

arr2 = np.array(["d", "e", "f"])

arr3 = np.concatenate((arr1, arr2))

print(arr3)
# joining  2darrays
arr4 = np.array([[1, 2], [3, 4]])

arr5 = np.array([[5, 6], [7, 8]])

arr6 = np.concatenate((arr4, arr5), axis=1)

print(arr6)
# splitting arrays
nwarr = np.array_split(arr, 5)
print(nwarr)

# searching from  Array

p = np.where(arr == 4)

print(p)

# searchsorted
n = np.searchsorted(arr, 17)
print(n)

# sorting arrays
print(np.sort(arr))

#That's all I had for you. Thank you
