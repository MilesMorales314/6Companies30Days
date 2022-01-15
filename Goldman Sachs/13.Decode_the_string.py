def decodedString(self, s):
    str = []
    for i in s:
        temp = []
        str.append(i)
        if i == ']':
            a = str.pop()
            while a != '[':
                a = str.pop()
                if a != '[':
                    temp.append(a)
            temp = temp[::-1]
            value = ''
            while str:
                b = str[-1]
                try:
                    int(b)
                    value += str.pop()
                except:
                    break
            str += (int(value[::-1]) * temp)
        
    return ''.join(str)