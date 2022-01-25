def isValid(self, mat):
    def isRow(m):
        for i in m:
            dp = [0]*10
            for j in i:
                if j and dp[j]:
                    return 0
                dp[j] = 1
        
        return 1
    
    def isColumn(m):
        for i in range(9):
            dp = [0]*10
            for j in range(9):
                if m[j][i] and dp[m[j][i]]:
                    return 0
                dp[m[j][i]] = 1
        
        return 1
    
    def is3x3(m):
        for a in range(0,9,3):
            for b in range(0,9,3):
                dp = [0]*10
                for i in range(3):
                    for j in range(3):
                        if m[a+i][b+j] and dp[m[a+i][b+j]]:
                            return 0
                        dp[m[a+i][b+j]] = 1
        
        return 1
    
    
    return isRow(mat) & isColumn(mat) & is3x3(mat)