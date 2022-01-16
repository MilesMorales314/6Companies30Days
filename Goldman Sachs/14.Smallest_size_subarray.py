def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    minLen = inf
    j = res = 0
    for i in range(len(nums)):
        res += nums[i]
        while res-nums[j] >= target:
            res -= nums[j]
            j += 1

        if res >= target:
            minLen = min(i-j+1, minLen)

    return 0 if minLen == inf else minLen