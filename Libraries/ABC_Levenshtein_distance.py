
# edit S to T
def Levenshtein_distance(S, T):
    # create and initialize DP table
    dp = [[i] + [0]*len(T) for i in range(len(S)+1)]
    for i in range(len(T)): dp[0][i+1] = i+1

    cost_ins = 1
    cost_del = 1
    cost_rep = 1

    for i in range(1, len(S)+1):
        for j in range(1, len(T)+1):
            # from upper -> delete
            tmp_del = dp[i-1][j] + cost_del

            # from left -> insert
            tmp_ins = dp[i][j-1] + cost_ins

            # fro upper left -> replace or nothing
            if S[i-1]==T[j-1]:
                tmp_rep = dp[i-1][j-1]
            else:
                tmp_rep = dp[i-1][j-1] + cost_rep
            
            dp[i][j] = min([tmp_del, tmp_ins, tmp_rep])

    return dp[-1][-1]