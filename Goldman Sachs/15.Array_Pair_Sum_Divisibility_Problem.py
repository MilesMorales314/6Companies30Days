def canPair(self, nums, k):
	dp = [0]*k
	for num in nums:
	    dp[num%k] += 1
    
    if dp[0] & 1 or (k & 1 == 0 and dp[k>>1] & 1):
        return False
    
    i = 1
    while i < k-i:
        if dp[i] != dp[k-i]:
            return False
        i += 1
    
    return True