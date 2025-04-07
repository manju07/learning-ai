from loops_practice import buble_sort

x = 1
x += 1
if x % 2 == 0:
    print("Odd")
else:
    print("Even")

# print("Hi, Learning learning-python")
# print(sys.version)

id = 1;
name = str("manjunath");
print(type(id))
print(type(name))

# assign multiple values at same time y
id, name = 1, "Manjunath"
print(id, name)

# splitting array to variables
employee = [1, "Manjunath"]
id, name = employee
print(id, name)

# assigning same value to multiple variables
x = y = z = "manju"
print(x, y, z)

# print output
print(x, y, z)

print(x + y + z)


def test_function(name, phone):
    print("\nExecuting testFunction")
    print(name, phone)


test_function("manjunath", "9886988915")

a = 2
b = 10

if a == 2 and b == 10:
    print("OK")


def function_new(a, b, c):
    print(a, b, c)


function_new(1, 2, 3)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
print(list1, list1[:5], list1[5:])

set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1}
print(set1)

set1 = set(list1)
print(set1)

print(buble_sort(list1))
