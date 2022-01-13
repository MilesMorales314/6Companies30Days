class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == "":
            return str2 
        elif str2 == "":
            return str1
        l1 = len(str1)
        l2 = len(str2)
        if l2 > l1:
            if str2.endswith(str1):
                return self.gcdOfStrings(str1, str2[:-l1]) 
        else:
            if str1.endswith(str2):
                return self.gcdOfStrings(str2, str1[:-l2])
        
        return ""