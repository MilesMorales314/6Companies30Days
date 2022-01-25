def colName (self, n):
    
    r = chr(64 + (n%26)) if n%26 else 'Z'
    if (n-1) // 26 == 0:
        return r
    
    return self.colName((n-1)//26) + r