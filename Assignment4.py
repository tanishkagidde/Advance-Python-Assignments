# Memoization
def fibonacci_memoization(n, dp):
    if n <= 1:
        return n

    if dp[n] != -1:
        return dp[n]

    dp[n] = fibonacci_memoization(n - 1, dp) + fibonacci_memoization(n - 2, dp)
    return dp[n]

# Tabulation
def fibonacci_tabulation(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

n = int(input("Enter value : "))

dp = [-1] * (n + 1)
memoization_result = fibonacci_memoization(n, dp)
tabulation_result = fibonacci_tabulation(n)

print("\nMemoization Answer :", memoization_result)
print("\nTabulation Answer  :", tabulation_result)

#OUTPUT
'''
Enter value : 8

Memoization Answer : 21

Tabulation Answer  : 21
'''
