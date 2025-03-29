import numpy as np

arr = np.array([1, 2, 3])
for x in arr:
    print(x)
print(arr, type(arr))

two_d_array = np.array([[1, 2, 3], [5, 4, 2]])

for i in range(len(two_d_array)):
    for j in range(len(two_d_array[i])):
        print(two_d_array[i, j], end=' ')
    print()

three_d_array = np.array([[[1, 2, 3], [4, 5, 6]], [[5, 6, 7], [9, 0, 1]]])
print('three_d_array[1][1][2]', three_d_array[1, 1, 2])
print('total dimensions', three_d_array.ndim)
print('shape', three_d_array.shape)
print('shape', three_d_array.reshape(-1), three_d_array.ndim)

# copy of array
copy_arr = three_d_array.copy()
print('copy_arr, copy_arr.ndim, copy_arr.base', copy_arr, copy_arr.ndim, copy_arr.base)

# view of array
view_arr = three_d_array.view()
print('view_arr, view_arr.ndim, view_arr.base', view_arr, view_arr.ndim, view_arr.base)

print(np.array([5, 1, 2], dtype='S'), end='\n\n')

three_d_array_f = three_d_array.astype('f')
print('three_d_array_f.dtype, three_d_array_f', three_d_array_f.dtype, three_d_array_f)


three_d_array_b = three_d_array.astype('bool')
print('three_d_array_b, three_d_array_b.dtype', three_d_array_b, three_d_array_b.dtype)

print('arr\n', np.array([1, 2, 3]))

print('2d array\n', np.array([[1,2], [3, 4], [5, 6]]), end='\n\n')

print('np.zeros(3)\n', np.zeros(3), end='\n\n')
print('np.zeros((3,3))\n', np.zeros((3, 3)), end='\n\n')

print('np.ones(3)\n', np.ones(3), end='\n\n')
print('np.ones((3,3))\n', np.ones((3,3)), end='\n\n')

print('np.eye(4)\n', np.eye(4))

print('np.arange(0, 10)\n',np.arange(0, 10))

print('np.arange(0, 10, 2)\n', np.arange(0, 10, 2))

print('np.random.rand(5)\n', np.random.rand(5)) # uniform distributed random points b/w 0 to 1
print('np.random.rand(5, 5)\n', np.random.rand(5,5)) # uniform distributed random points b/w 0 to 1 2D

print('np.random.randn(5)\n', np.random.randn(5)) # standard distributed random points center around 0
print('np.random.randn(5, 5)\n', np.random.randn(5, 5)) # above and 2D



print('np.random.randint(10)\n', np.random.randint(10))
print('np.random.randint(0,10, 5)\n', np.random.randint(0,10, 5))


print('np.linspace(0, 5, 10)\n', np.linspace(0, 5, 10)) # Distributed 10 points between 0 to 5


rarr = np.random.randint(0, 100, 10)
print('rarr\n', rarr)
print('rarr.max()\n', rarr.max())
print('rarr.min()\n', rarr.min())
print('rarr.argmax()\n', rarr.argmax()) # index of max
print('rarr.argmin()\n', rarr.argmin()) # index of min
print('rarr.shape\n', rarr.shape)

rarr = rarr.reshape(5, 2)
print('rarr.shape after reshape\n', rarr.shape)
print('rarr\n', rarr)

print('rarr.dtype\n', rarr.dtype)


arr = np.random.randint(0 , 10, 10)
print('arr\n', arr)

arr[0:5] = 100
print('arr[0:5] = 100, arr\n', arr)

# slice of array is reference to original
slice_of_arr = arr[0:5]
arr[0:5] = 1
print('arr[0:5] = 1, arr', arr, '\nslice_of_arr', slice_of_arr, end='\n\n')

# copy of array
copy_of_arr = arr.copy()
arr[0:5] = 100
print('arr[0:5] = 100, arr\n', arr, '\ncopy_arr', copy_of_arr, end='\n\n')


# 2D array
two_d_array = np.random.randint(0, 100, 25).reshape(5, 5)
print('\ntwo_d_array\n', two_d_array)

# slicing in 2D
print('\ntwo_d_array[2:4, 1:3]\n', two_d_array[2:4, 1:3])
print('\ntwo_d_array[2:, 3:]\n', two_d_array[2:, 3:])

# array with operators
arr = np.arange(10)
print('arr\n', arr)
bool_arr = arr > 5
arr = arr[bool_arr]
print('arr', arr, '\nbool_arr', bool_arr)

print('arr + 10', arr + 10)
print('arr * 2', arr * 2)
print('arr/arr', arr/arr)

# universal functions
print('np.sqrt(arr)\n', np.sqrt(arr))
print('np.max(arr)\n', np.max(arr))
print('np.min(arr)\n', np.min(arr))

