print("Tuple array cannot be modified and its ordered")
array = [1, 2, 3]
print("Normal array: ", array)

tupleArray = (1, 2, 3)
print("Tuple array: ", tupleArray)

array.append(4)
print("Normal array after appending: ", array)

print("Different dtype in tuple : ", ("abc", 34, True, 40, "male"))

tuple1 = ("abc")
tuple2 = ("abc",)
print("Single record is not tuple : ", type(tuple1))
print("Single record with comma is tuple : ", type(tuple2))

# tupleArray[1] = 100 # 'tuple' object does not support item assignment
array[1] = 100
print("List can be modified but not tuple: ", array)
tupleArray += tupleArray
print("Tuple can be added with another tuple: ", tupleArray)
