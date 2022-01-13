class Solution:
    def Anagrams(self, words, n):
        memo = {}
        s2 = set()
        res = []
        
        for word in words:
            s = tuple(sorted(word))
            if s in memo:
                memo[s] += [word]
                s2.add(s)
            
            if s not in memo:
                memo[s] = [word]
        
        return memo.values()