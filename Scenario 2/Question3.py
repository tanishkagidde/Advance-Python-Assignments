'''
	3. Climbing Stairs Problem									
										
	Develop a Python program to determine the number of distinct ways to climb a staircase.									
										
	Requirements									
		Accept the number of stairs.								
		A person may climb either 1 or 2 stairs at a time.								
		Use Dynamic Programming.								
		Display the total number of ways.								
										
'''
class StairClimber:
    @staticmethod
    def climb_stairs(n: int) -> int:
        """
        Calculates the number of distinct ways to climb n stairs
        taking either 1 or 2 steps at a time using dynamic programming.
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        # DP array to store the number of ways to reach each step
        dp = [0] * (n + 1)
        dp[1] = 1 
        dp[2] = 2  
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


# Main Program
if __name__ == "__main__":
    try:
        num_stairs = int(input("Enter the total number of stairs: "))
        
        if num_stairs < 0:
            print("Please enter a non-negative integer.")
        else:
            total_ways = StairClimber.climb_stairs(num_stairs)
            print(f"\nTotal distinct ways to climb {num_stairs} stair(s): {total_ways}")
            
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
'''
OUTPUT :
Enter the total number of stairs: 6

Total distinct ways to climb 6 stair(s): 13
'''
