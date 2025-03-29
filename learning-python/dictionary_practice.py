dict1 = {
    "name": "Manjunath",
    "age": 22,
    "salary": 20000
}

print(dict1)
print("$$$name", dict1["name"])

for key in dict1.keys():
    print(key, dict1[key])


def dict_function(dict1):
    print("calling dict_function")
    for key in dict1.keys():
        print(key, dict1[key])


dict_function(dict1)