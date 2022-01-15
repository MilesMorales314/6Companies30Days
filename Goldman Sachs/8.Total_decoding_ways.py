def CountWays(str):
    n = len(str)
    dp = [1]*(n+1)
    mod = 10**9+7
    
    if n <= 1 and str != '0':
        return 1
    
    if str[0] == '0' :
        return 0
    
    for i in range(2, n+1):
        u, pu = str[i-2], str[i-1]
        if u > '0' and pu > '0':
            if u+pu <= '26':
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
        else:
            if u == '0':
                if pu == '0':
                    return 0
                else:
                    dp[i] = dp[i-1]
            else:
                if u > '2':
                    return 0
                else:
                    dp[i] = dp[i-2] 
    return dp[n]%mod