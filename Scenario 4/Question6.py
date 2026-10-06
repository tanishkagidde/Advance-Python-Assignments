'''
OUESTION 6 :
6. Cricket Statistics Analysis System					
					
Develop a Python application to analyze cricket player statistics.					
					
Requirements					
	Create a NumPy array of runs scored by players.				
	Calculate average, highest, and lowest runs.				
	Create a Pandas DataFrame.				
	Display players scoring more than 5000 runs.				
'''

import numpy as np
import pandas as pd

# 1. Sample cricket player data
player_data = {
    "Player": [
        "Virat Kohli",
        "Joe Root",
        "Steve Smith",
        "Kane Williamson",
        "Babar Azam",
        "Ben Stokes",
    ],
    "Matches": [113, 140, 109, 100, 52, 105],
    "Runs": [8848, 11736, 9685, 8781, 3898, 6320],
}

# 2. Create a NumPy array of runs scored by players
runs_array = np.array(player_data["Runs"])

# 3. Calculate average, highest, and lowest runs using NumPy
avg_runs = np.mean(runs_array)
max_runs = np.max(runs_array)
min_runs = np.min(runs_array)

print("--- Statistical Summary (NumPy) ---")
print(f"Average Runs: {avg_runs:.2f}")
print(f"Highest Runs: {max_runs}")
print(f"Lowest Runs:  {min_runs}")
print("-" * 35)

# 4. Create a Pandas DataFrame
df = pd.DataFrame(player_data)

print("\n--- Full Cricket Statistics DataFrame ---")
print(df)

# 5. Display players scoring more than 5000 runs
high_scorers = df[df["Runs"] > 5000]

print("\n--- Players Scoring More Than 5000 Runs ---")
print(high_scorers)

'''
OUTPUT :
--- Statistical Summary (NumPy) ---
Average Runs: 8211.33
Highest Runs: 11736
Lowest Runs:  3898
-----------------------------------

--- Full Cricket Statistics DataFrame ---
            Player  Matches   Runs
0      Virat Kohli      113   8848
1         Joe Root      140  11736
2      Steve Smith      109   9685
3  Kane Williamson      100   8781
4       Babar Azam       52   3898
5       Ben Stokes      105   6320

--- Players Scoring More Than 5000 Runs ---
            Player  Matches   Runs
0      Virat Kohli      113   8848
1         Joe Root      140  11736
2      Steve Smith      109   9685
3  Kane Williamson      100   8781
5       Ben Stokes      105   6320
'''
