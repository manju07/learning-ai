data = [1, 2, 3, 4]

for x in data:
    print(x, end=" ")

print(end="\n\n")

for x in range(len(data)):
    print(x, data[x])

print(type('data'))

if 2 % 2 == 0 and 1 % 1 == 1:
    print('condition is true')
elif 1 % 1 == 0:
    print('condition is false')
else:
    print("executing else part")

if not 1 % 1 == 1:
    print("if not 1%1 == 1, condition is true")

print("While loop")

index = 0
while index <= 100:
    print(index, end=" ")
    index += 1

print(end="\n\n")
set1 = {1, 4, 3, 1}
print(set1)

from class_practice import Student

s1 = Student("M", "A", "CS")
print(s1)

print(2 ** 6)  # 2^6

print((True and True) or (True or False))

data = 1
if data > 1:
    print('data > 1')
elif data < 1:
    print('data < 1')
else:
    print('data == 1')


def square(num):
    return num ** 2


print('list(map(square, set1))', set1, list(map(square, set1)))

# Map and lambda
print('list(map(lambda num: num ** 2, set1))', set1, list(map(lambda num: num ** 2, set1)))

# Filter and lambda
print('list(filter(lambda num: num%2 == 1, set1))', set1, list(filter(lambda num: num % 2 == 1, set1)))
