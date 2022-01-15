def getNthUglyNo(self,n):
	u = []
    i2 = i3 = i5 = 0
    umin = 1
    for _ in range(n-1):
        u.append(umin)
        u2, u3, u5 = 2*u[i2], 3*u[i3], 5*u[i5]
        umin = min(u2, u3, u5)
        if u2 == umin:
            i2 += 1
        if u3 == umin:
            i3 += 1
        if u5 == umin:
            i5 += 1
    
    return umin