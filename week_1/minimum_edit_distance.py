# Levenshtein Distance Algorithm
def editDistance(str1, str2):
    m = len(str1)
    n = len(str2)
    delete_cost = 1
    insertion_cost = 1
    replacement_cost = 2
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            else:
                dp[i][j] = min(
                    dp[i][j - 1] + delete_cost,
                    dp[i - 1][j] + insertion_cost,
                    dp[i - 1][j - 1] + (replacement_cost if str1[i - 1] == str2[j - 1] else 0)
                )
    return dp[m][n]


string1 = 'go'
string2 = 'to'
print(editDistance(string1, string2))
