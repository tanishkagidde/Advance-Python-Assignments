def longest_common_subsequence(str1, str2):
    m = len(str1)
    n = len(str2)

    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i = m
    j = n
    lcs = ""

    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs = str1[i - 1] + lcs
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs, dp[m][n]


sequence1 = input("Enter the first sequence: ")
sequence2 = input("Enter the second sequence: ")

lcs, length = longest_common_subsequence(sequence1, sequence2)

print("\nLongest Common Subsequence:", lcs)
print("Length of LCS:", length)

'''

OUTPUT :

Enter the first sequence: ABCDGH
Enter the second sequence: AEDFHR

Longest Common Subsequence: ADH
Length of LCS: 3

Enter the first sequence: AGGTAB
Enter the second sequence: GXTXAYB

Longest Common Subsequence: GTAB
Length of LCS: 4

Enter the first sequence: ABCDEF
Enter the second sequence: ACE

Longest Common Subsequence: ACE
Length of LCS: 3

Enter the first sequence: HELLO
Enter the second sequence: YELLOW

Longest Common Subsequence: ELLO
Length of LCS: 4

Enter the first sequence: COMPUTER 
Enter the second sequence: HOUSE

Longest Common Subsequence: OUE
Length of LCS: 3

Enter the first sequence: PYTHON
Enter the second sequence: TYCOON

Longest Common Subsequence: TON
Length of LCS: 3

Enter the first sequence: PROGRAM
Enter the second sequence: GRAPE

Longest Common Subsequence: GRA
Length of LCS: 3

Enter the first sequence: ENGINEERING
Enter the second sequence: GREENING

Longest Common Subsequence: GEEING
Length of LCS: 6

Enter the first sequence: BANANA
Enter the second sequence: ATANA

Longest Common Subsequence: AANA
Length of LCS: 4

Enter the first sequence: ABCXYZ
Enter the second sequence: XYZABC

Longest Common Subsequence: XYZ
Length of LCS: 3

'''
