fruits = ("apple", "mango", "papaya", "pineapple", "cherry", "kiwi")

print("Starred expression in second:")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

print("Starred expression in last:")
(green, tropic, *red) = fruits

print(green)
print(tropic)
print(red)

for x in fruits:
    print("Printing fruits via for loop: ", x)
