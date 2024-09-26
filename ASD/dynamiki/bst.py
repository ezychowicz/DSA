class BNode:
    def __init__( self, value ):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value

def insert(root, key):
    if root is None:
        return BNode(key)
    else:
        if root.value == key:
            return root
        elif root.value < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


#10, 3, 15, 11, 17, -1, -5, 0
root = insert(None, 10)
root = insert(root, 3)
root = insert(root, 15)
root = insert(root, 11)
root = insert(root, 17)
root = insert(root, -1)
root = insert(root, -5)
root = insert(root, 0)

def not_root(l):
    suma = 0
    while l.right == None and l.left != None:
        l = l.left
    if l.left == None and l.right == None: #jestesmy w lisciu 
        l = l.parent
        print(l.value)
        suma += l.value
    elif l.right != None: #jestesmy w nie-lisciu i istnieje lewe dziecko: trzeba jak najszybciej usunac
        suma += l.value
    return suma
def cutthetree(root):
    l = root.left
    r = root.right
    return not_root(l) + not_root(r)
    
print(cutthetree(root))


     
