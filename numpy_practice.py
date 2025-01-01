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
