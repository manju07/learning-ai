print("Hi hello")

if 1 % 1 == 1:
    print(True)
elif 1 % 2 == 0:
    print(False)
else:
    print("Nothing")


def sum_of_two(a, b):
    return a + b;


print(sum_of_two(10, 20));


def sum_of_arr_ele(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum


print(sum_of_arr_ele([10, 20, 30]))


def remove_duplicates(arr):
    unique_set = set()
    for i in range(len(arr)):
        unique_set.add(arr[i])
    return unique_set


print(remove_duplicates([1, 2, 3, 4, 2, 3, 9, 10]))

new_set = {1, 2, 3, 4, 9, 10, 8}

if new_set.__contains__(1):
    new_set.remove(1)

# new_set.
print(new_set)
