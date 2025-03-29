str1 = 'str1'
str2 = "str2"

print(str1, str2)

print(end="\n\n")
print(str1[2])

for i in range(len(str1)):
    print(str1[i], end=" ")


first_name = 'Manjunath'
last_name = 'Asundi'

print(end="\n\n")
print('My first name is {} and last name is {}'.format(first_name, last_name))
print('My first name is {two} and last name is {one}, Thanks {two}'.format(two=first_name, one=last_name))


