def findTwoElement( self,arr, n):
    x = a = b = 0
    s = set()
    for i in range(n):
        x ^= (i+1) ^ arr[i]
    
    for i in range(n):
        if arr[abs(arr[i])-1] < 0:
            a = abs(arr[i])
            break
        arr[abs(arr[i])-1] *= -1
    
    b = x ^ a
    
    return a, b