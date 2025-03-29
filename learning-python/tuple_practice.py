# can't modify the mode

tuple1 = (1, 2, 3)
print(tuple1)
print(len(tuple1))

#  with item
tuple2 = (1, )
print(tuple2)

print(type(tuple2))

tuple3 = (1, 2, 3, "manju", 1.0, True, None)
print(tuple3)

tuple4 = tuple((1, 2, 3, "manju", 1.0, True, None))
print(tuple4)

tuple4 = (1, 2, 3, "manju", 1.0, True, None)
(a, b, c, *d) = tuple4
print(a, b, c, d)
