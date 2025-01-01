def selection_sort(arr):
    print("selection sort")
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

print(selection_sort([100, 2, 30, 4, 25, 6, 7, 8, 9]))


# print even numbers
def print_even_numbers(range):
    a = 0;
    while a <= range:
        if a % 2 == 0:
            print(a)
        a += 1


# print_even_numbers(100)


def increment_by_data(data, max):
    print("increment_by_input", data, range)
    for i in range(0, max, data):
        print(i)


# increment_by_data(3, 100)

# k range (0, n)
# i = 0, j = 1, compare values and swap
# i = 1, j = 2, compare values and swap


def buble_sort(arr):
    print("bubble_sort")
    for i in range(len(arr)):
        j, k = 0, 1
        while j < (len(arr) - 1) and k < len(arr):
            if arr[j] > arr[k]:
                arr[j], arr[k] = arr[k], arr[j]
            j += 1
            k += 1
    return arr


print(buble_sort([100, 2, 30, 4, 25, 6, 7, 8, 9]))
