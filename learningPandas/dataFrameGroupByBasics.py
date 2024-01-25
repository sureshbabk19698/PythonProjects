import pandas as pd

data = {'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales': [200, 120, 340, 124, 243, 350]}
df = pd.DataFrame(data)
print(df)

g_company = df.groupby("Company")
print(g_company)  # <pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000020FFCF080A0>

print(g_company.mean(numeric_only=True))
print(g_company.std(numeric_only=True))
print("Min: ")
print(g_company.min(numeric_only=True))
print("Max: ")
print(g_company.max(numeric_only=True))
print("Count: ")
print(g_company.count())
#         count   mean         std    min     25%    50%     75%    max
# Company
# FB        2.0  296.5   75.660426  243.0  269.75  296.5  323.25  350.0
# GOOG      2.0  160.0   56.568542  120.0  140.00  160.0  180.00  200.0
# MSFT      2.0  232.0  152.735065  124.0  178.00  232.0  286.00  340.0
desc = g_company.describe()
print(desc.loc[['FB', 'GOOG']])

# print(df.head(5))
print(df['Company'])
print("Unique Elements in column: ", df['Company'].unique())
print("Unique Elements count in column: ", df['Company'].nunique())
