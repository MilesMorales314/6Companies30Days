def maxTen(nums: list):
    lbound = min(nums[:10])
    res = nums[:10]
    
    for num in nums[10:]:
        if num > lbound:
            res.remove(lbound)
            res.append(num)
            lbound = min(res)
    
    return res