set1 = {1, 2, 3}
print("set1", set1)

# noinspection PySetFunctionToLiteral
set2 = set((1, 2, 3))
print("set2", set2)

for x in set1:
    print(x)

for x in set2:
    print(x)

print("1 in set1", 1 in set1)
print("1 not in set1", 1 not in set1)

set1.add(4)

set1.update(set2)
print("update", set1)

print("union", {1, 2, 3}.union({1, 2, 3, 4}))

set1.remove(4)
set1.discard(4)

print("union multiple sets", {1, 2, 3}.union({1, 2, 3, 4}, {1, 2, 3, 5}))

print("intersection", {1, 2, 3}.intersection({1, 2, 3, 4}, {1, 2, 3, 5}))

print("difference", {1, 2, 3, 4, 5, 6}.difference({1, 2, 3, 4}, {1, 2, 3, 5}))

print("symmetric_difference", {1, 2, 3, 4, 5, 6}.symmetric_difference({1, 2, 3, 4}))

print(" | == union", {1, 2, 3} | {1, 2, 3, 4})
print(" & == intersection", {1, 2, 3} & {1, 2, 3, 4})
print(" - == difference", {1, 2, 3, 4, 5, 6} - {1, 2, 3, 4} - {1, 2, 3, 5})

# ^ == symmetric_difference
