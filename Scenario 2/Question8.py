	'''
  8. Longest Common Substring									
										
	Develop a Python program to determine the length of the longest common substring between two strings.									
										
	Requirements									
		Accept two strings.								
		Use Dynamic Programming.								
		Display the length of the longest common substring.					
'''
class SubstringFinder:
    @staticmethod
    def longest_common_substring(str1: str, str2: str) -> int:

        m, n = len(str1), len(str2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_length = 0

        # Build the DP table bottom-up
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_length = max(max_length, dp[i][j])
                else:
                    dp[i][j] = 0 

        return max_length


# --- Main Program ---
if __name__ == "__main__":
    string1 = input("Enter the first string: ").strip()
    string2 = input("Enter the second string: ").strip()

    result_length = SubstringFinder.longest_common_substring(string1, string2)
    
    print(f"\nLength of the Longest Common Substring: {result_length}")
'''
OUTPUT :

Enter the first string: programming
Enter the second string: grammer

Length of the Longest Common Substring: 5

Enter the first string: abcde
Enter the second string: fghik

Length of the Longest Common Substring: 0
'''
