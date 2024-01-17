print("Dictionary is ordered and mutable")
map = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020,
    "members": [1, 2, 3]
}
print("Printing map: ", map)
print("Length of map: ", len(map))

print("Map get key: ", map.get("yearr"))  # if key is not present will return None
# print("Map get key: ", map["yearr"])  # if key is not present will throw KeyError: 'yearr'

map["yearr"] = "dummy"
map.update({"members": 5})  # will add/update existing key with new value

print("Items in map: ", map.items())
print("Keys in map: ", map.keys())
print("Values in map: ", map.values())

print("Popped item: ", map.pop("members"))
print("Pop last inserted item: ", map.popitem())

emptyMap = {}

# print("Popped item: ", emptyMap.pop("members")) #KeyError: members
# print("Pop last inserted item: ", emptyMap.popitem()) #KeyError: 'popitem(): dictionary is empty'

for x in map:  # for x in map.keys(): both are same
    print("Iterating key ", x, "and value: ", map[x])

for x in map.items():  # equivalent to Map.Entry<> entry: map.entrySet()
    print("Iterating item : ", x)

stateMap = {"India": "Delhi", "Belgium": "Brussels", "France": "Pair"}
nestedMap = {
    "Country": stateMap,
}

print("Accessing nested map ", nestedMap["Country"]["India"])

x = ('key1', 'key2', 'key3')
y = 0

createDictWithEmptyOrDefaultValue = dict.fromkeys(x, y)
print("Printing fromkeys map ", createDictWithEmptyOrDefaultValue)
