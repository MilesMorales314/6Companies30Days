def skipMdeleteN(self, head, M, N):
    temp=head
   
    list1=[]
    
    while temp!=None:
        list1.append(temp)
        temp=temp.next
    
    l=len(list1)  
    
    head = temp = Node(0)
    n = i = 0
    
    while i < l:
        if n<M:
           temp.next = list1[i]
           temp = temp.next
           n += 1
           i += 1
        else:
           n = 0
           i += N
    temp.next = None