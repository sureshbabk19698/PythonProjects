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

ser2['a'] = 'a'
# Merging column dtype should be same
# print("Merging Series", ser1 + ser2)  # TypeError: unsupported operand type(s) for +: 'float' and 'str'
