def displayContacts(self, n, contact, s):
    res = []
    temp = contact.copy()
    query = ''
    for q in s:
        query += q
        res.append([])
        track = set()
        for c in temp:
            if c.startswith(query) and c not in track:
                res[-1].append(c)
            track.add(c)
        
        res[-1].sort()
        temp = res[-1]
        
        if not res[-1]:
            res[-1].append('0')
    
    return res