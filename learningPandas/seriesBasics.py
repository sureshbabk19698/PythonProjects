import pandas as pd
import numpy as np

labels = ['a', 'b', 'c']
my_list = [10, 20, 30]
arr = np.array([10, 20, 30])
d = {'a': 10, 'b': 20, 'c': 30}

ser1 = pd.Series(data=my_list, index=labels)
ser2 = pd.Series(d)
print("Series 1", ser1)
print("Series 2", ser2)

print("Accessing via index", ser1['a'])

ser2['d'] = 'd'
print("Merging Series", ser1 + ser2)

ser2['a'] = [14, 134]
# Merging column dtype should be same
# print("Merging Series", ser1 + ser2)  # TypeError: unsupported operand type(s) for +: 'float' and 'str'
for x in ser2.items():
    print(x)

ser3 = pd.Series(data=[5, 10, 15, 20, 10], index=['a', 'b', 'a', 'b', 'a'])
print(ser3.sum())
print(ser3.groupby(level=0).sum())  # level = 0 is index
