import numpy as np
import pandas as pd

np.random.seed(42)

# 1. Create a Series containing ten random numbers
data = np.random.randint(1, 100, size=10)
series = pd.Series(data, name="RandomNumbers")

print("--- Original Pandas Series ---")
print(series)
print()

# 2. Indexing Operations
print("--- Indexing Operations ---")
print(f"First element (Index 0): {series[0]}")
print(f"Fourth element (Index 3): {series[3]}")
print("Slice (Index 2 to 5):")
print(series[2:6])
print()

# 3. Filtering Operations
print("--- Filtering Operations ---")
# Filter values greater than 50
filtered_series = series[series > 50]
print("Values greater than 50:")
print(filtered_series)
print()

# 4. Statistical Operations
print("--- Statistical Operations ---")
print(f"Mean:    {series.mean():.2f}")
print(f"Median:  {series.median():.2f}")
print(f"Minimum: {series.min()}")
print(f"Maximum: {series.max()}")

'''
--- Original Pandas Series ---
0    52
1    93
2    15
3    72
4    61
5    21
6    83
7    87
8    75
9    75
Name: RandomNumbers, dtype: int64

--- Indexing Operations ---
First element (Index 0): 52
Fourth element (Index 3): 72
Slice (Index 2 to 5):
2    15
3    72
4    61
5    21
Name: RandomNumbers, dtype: int64

--- Filtering Operations ---
Values greater than 50:
0    52
1    93
3    72
4    61
6    83
7    87
8    75
9    75
Name: RandomNumbers, dtype: int64

--- Statistical Operations ---
Mean:    62.90
Median:  73.50
Minimum: 15
Maximum: 93
'''
