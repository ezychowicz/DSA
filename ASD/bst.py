class Node:
    def __init__( self, key, parent ):
        self.left = None # lewe poddrzewo
        self.right = None # prawe poddrzewo
        self.parent = parent # rodzic
        self.key = key # wartość wierzchołka
        self.x = None # pole do wykorzystania przez studentów

def predecessor(p):
    if p.left != None:
        p = p.left
        while p.right != None:
            p = p.right
        return p
    else:
        while p.parent != p:
            p, prev = p.parent, p
            if p.right == prev:
                return p
    
def succesor(p):
    if p.right != None:
        p = p.right
        while p.left != None:
            p = p.left
        return p
    else:
        while p.parent != p:
            p, prev = p.parent, p
            if p.left == prev:
                return p
T = []
def traverse(p): #stworz posortowaną tablice z BST
    global T
    if p.left != None:
        traverse(p.left)
    T.append(p)
    if p.right != None:
        traverse(p.right)
    
        