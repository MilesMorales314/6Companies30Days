    def countSubArrayProductLessThanK(self, a, n, k):
        start = 0
        end = 0
        p = 1
        count = 0
        while end < n:
            p *= a[end]
            if p >= k:
                while start < end and p >= k:
                    p //= a[start]
                    start += 1
            if p < k:
		count += end - start + 1
            end += 1
        
        return count