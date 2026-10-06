'''
QUESTION :
8. Grocery Store Analysis System					
					
Develop a Python application to analyze grocery inventory.					
					
Requirements					
	Create a NumPy array of product prices.				
	Calculate mean, median, maximum, and minimum price.				
	Create a Pandas DataFrame.				
	Display grocery items having quantity less than 10.				
  '''
import numpy as np
import pandas as pd

# 1. Sample grocery inventory data
inventory_data = {
    "Item": [
        "Milk",
        "Bread",
        "Eggs (dozen)",
        "Butter",
        "Cheese",
        "Apples (kg)",
        "Rice (5kg)",
    ],
    "Price": [60.0, 40.0, 75.0, 250.0, 180.0, 120.0, 350.0],
    "Quantity": [15, 8, 25, 5, 12, 6, 4],
}

# 2. Create a NumPy array of product prices
prices_array = np.array(inventory_data["Price"])

# 3. Calculate mean, median, maximum, and minimum price
mean_price = np.mean(prices_array)
median_price = np.median(prices_array)
max_price = np.max(prices_array)
min_price = np.min(prices_array)

print("--- Price Analysis (NumPy) ---")
print(f"Mean Price:   ₹{mean_price:.2f}")
print(f"Median Price: ₹{median_price:.2f}")
print(f"Maximum Price: ₹{max_price:.2f}")
print(f"Minimum Price: ₹{min_price:.2f}")
print("-" * 32)

# 4. Create a Pandas DataFrame
df = pd.DataFrame(inventory_data)

print("\n--- Full Inventory DataFrame ---")
print(df)

# 5. Display grocery items having quantity less than 10
low_stock_items = df[df["Quantity"] < 10]

print("\n--- Low Stock Items (Quantity < 10) ---")
print(low_stock_items)

'''
OUTPUT :
--- Price Analysis (NumPy) ---
Mean Price:   ₹153.57
Median Price: ₹120.00
Maximum Price: ₹350.00
Minimum Price: ₹40.00
--------------------------------

--- Full Inventory DataFrame ---
           Item  Price  Quantity
0          Milk   60.0        15
1         Bread   40.0         8
2  Eggs (dozen)   75.0        25
3        Butter  250.0         5
4        Cheese  180.0        12
5   Apples (kg)  120.0         6
6    Rice (5kg)  350.0         4

--- Low Stock Items (Quantity < 10) ---
          Item  Price  Quantity
1        Bread   40.0         8
3       Butter  250.0         5
5  Apples (kg)  120.0         6
6   Rice (5kg)  350.0         4
'''
