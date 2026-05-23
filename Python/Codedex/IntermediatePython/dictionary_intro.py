dictionary = {
    "key1" : "value1",
    "key2" : "value2",
    "key3" : "value3"
}
print(dictionary)
print(dictionary["key1"])
print(dictionary["key2"])
print(dictionary["key3"])
dictionary["key4"] = "value4"
print(dictionary)
dictionary["key1"] = "new_value1"
print(dictionary)
del dictionary["key2"]
print(dictionary)
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())