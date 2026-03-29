def edit_distance(s1, s2):
    m = len(s1)
    n = len(s2)

    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j],     # delete
                                   dp[i][j-1],     # insert
                                   dp[i-1][j-1])   # replace

    return dp[m][n]


# Example
print(edit_distance("cat", "cut"))


def weighted_edit(s1, s2):
    m = len(s1)
    n = len(s2)

    insert_cost = 1
    delete_cost = 1
    replace_cost = 2   # just change this value if needed

    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(m+1):
        dp[i][0] = i * delete_cost
    for j in range(n+1):
        dp[0][j] = j * insert_cost

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                cost = 0
            else:
                cost = replace_cost

            dp[i][j] = min(dp[i-1][j] + delete_cost,
                           dp[i][j-1] + insert_cost,
                           dp[i-1][j-1] + cost)

    return dp[m][n]


# Example
print(weighted_edit("cat", "cut"))
