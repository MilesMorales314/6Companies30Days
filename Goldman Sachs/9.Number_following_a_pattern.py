def printMinNumberForPattern(self,S):
    res = temp = num = running = 1
    
    for I in S:
        if I == 'I':
            res = (res*10)+num+1
            running = num+1
            temp = 1
        if I == 'D':
            res += temp
            res = (res*10)+ running
            temp = (temp*10)+1
        num += 1
    
    return res