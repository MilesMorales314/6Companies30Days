def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
    def checkInter(a, b, c, d):
        m = max(a, b, c, d)
        n = min(a, b, c, d)
        return (b-a+d-c) > m - n
    
    return checkInter(rec1[0], rec1[2], rec2[0], rec2[2]) and checkInter(rec1[1], rec1[3], rec2[1], rec2[3])