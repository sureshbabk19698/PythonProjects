print("Sets are unordered and modifiable but the elements in set must be immutable ")
print("Sets cannot be accessed via index, since its unordered ")

setList = {"abc", 1, "a", "b", "a"}
print(setList)
setList.add(5)
print(setList)

set1 = {"apple", "banana", "cherry", True, 1, False, 0, 2}
print(set1)  # True and 1 considered as same False and 0 considered as same

# elements in set must be immutable
# set2 = {"apple", "banana", ['banana']}  #TypeError: unhashable type: 'list'
set3 = {"apple", "banana", tuple(('banana',))}
print(set3)

x = set([1, 2, 3])
y = x
print("After assigning object reference: ", x is y)  # True
y = x.copy()
print("After copying object: ", x is y)  # False

x.remove(3)
print("After removing 3, set: +", x)
# print("After removing 3, set: +", x[2]) # TypeError: 'set' object is not subscriptable
