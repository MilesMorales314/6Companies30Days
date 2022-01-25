#Function to serialize a tree and return a list containing nodes of tree.
def serialize(root, A):
    if not root:
        return
    
    serialize(root.left,A)
    A.append(root.data)
    serialize(root.right,A)
    
#Function to deserialize a list and construct the tree.   
def deSerialize(A):
    r = temp = Node(0)
    for i in A:
        temp.right = Node(i)
        temp = temp.right
    return r.right