def encode(arr):
    initial = arr[0]
    count = 0
    res = ''
    
    for letter in arr:
        if initial == letter:
            count += 1
        else:
            res += initial + str(count)
            initial = letter
            count = 1
    
    return res + initial + str(count)