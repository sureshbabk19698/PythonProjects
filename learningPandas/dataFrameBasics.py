import pandas as pd
import numpy as np

array = np.arange(1, 21).reshape(5, 4)
#     W   X   Y   Z
# A   1   2   3   4
# B   5   6   7   8
# C   9  10  11  12
# D  13  14  15  16
# E  17  18  19  20

df = pd.DataFrame(array, index='A B C D E'.split(), columns='W X Y Z'.split())
print(df)

print("Fetching specific  c: ", df['X'], ' column type: ', type(df['X']))
print("Fetching specific columns by comma seperator: ", df[['X', 'Z']])

df['sum'] = df['W'] + df['Y']
print("Sum: ", df['sum'])

# axis=1 --> columns
# axis=0 --> rows or index
df.drop('sum', axis=1, inplace=True)
# print("After dropping sum column: ", df['sum']) #KeyError: 'sum'
df.drop('E', axis=0, inplace=True)
print("DF: ", df)

# accessing index or rows
#    W  X  Y  Z
# A  1  2  3  4
# B  5  6  7  8
print("Accessing multiples rows: ", df.loc[['A', 'B']])
# W     9
# X    10
# Y    11
# Z    12
print("Accessing rows by index location: ", df.iloc[2])
# 1
print("Accessing single row * column record: ", df.loc['A', 'W'])
#    W  Y
# A  1  3
# B  5  7
print("Accessing range of rows * columns: ", df.loc[['A', 'B'], ['W', 'Y']])

print(df > 5)  # return True or False for all values
print(df[df > 5])  # return Values if True
#     W   X   Y   Z
# B   5   6   7   8
# C   9  10  11  12
# D  13  14  15  16
print(df[df['X'] > 5])  # return Values if True
print(df[df['W'] > 5]['Y'])
print(df[df['W'] > 5][['X', 'Y']])

print()
print(df[(df['W'] > 1) & (df['Y'] > 7)])

print(df.reset_index())  # not inplace
print(df)

# print(df.set_index("States")) #KeyError: "None of ['States'] are in the columns"
df['States'] = 'CA NY WY OR'.split()
print(type(df['States'].values))  # <class 'numpy.ndarray'>
print(df.set_index("States"))

df1 = pd.DataFrame({'A': [1, 2, np.nan],
                    'B': [5, np.nan, np.nan],
                    'C': [1, 2, 3]})
print(df1)
print(df1.dropna(axis=1))
print(df1.dropna())
print(df1.dropna(thresh=2))
print(df1.fillna(value='Dummy'))

print(df1['A'].fillna(value=df1['A'].mean()))