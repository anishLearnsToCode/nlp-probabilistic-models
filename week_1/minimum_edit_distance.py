# Levenshtein Distance Algorithm
def editDistance(source, target):
    m = len(source)
    n = len(target)
    deletion_cost = 1
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
                    dp[i][j - 1] + deletion_cost,
                    dp[i - 1][j] + insertion_cost,
                    dp[i - 1][j - 1] + (0 if source[i - 1] == target[j - 1] else replacement_cost)
                )
    return dp[m][n]


string1 = 'stay'
string2 = 'play'
print(editDistance(string1, string2))
