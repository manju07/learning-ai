list1 = [1, 2, 3]

print(list1)

# loop thru data
for data in list1:
    print(data, end=' ')

print()

# loop thru index
for index in range(len(list1)):
    print(list1[index], end=' ')

print()

list1.append(4)
print(list1)

list1.append('Manju')
print(list1)

list2 = [2, 3, 4, ['a', ['b', 1]]]
print(list2[3][1][0], list2[3][1][1])

print((list2[1:]))
print((list2[:]))
print((list2[:3]))
