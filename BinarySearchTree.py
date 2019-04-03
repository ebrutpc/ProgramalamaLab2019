import random

class myNode(object):
    def __init__(self,v=0):
        self.val=v
        self.left=None
        self.right=None

class my_Tree(object):
    def __init__(self):
        self.root=myNode(250)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end=" ")
        inorder(root.right)

def insert(root,node):
    if root is None:
        root=node
    else:
        if root.val<node.val:
            if root.right is None:
                root.right=node
            else:
                insert(root.right,node)
        else:
            if root.left is None:
                root.left=node
            else:
                insert(root.left,node)
def test():
    numbers=[]
    for x in range(5):
        numbers.append(random.randint(1,101))
        print(numbers)
        Tree_1=my_Tree()
        for n in numbers:
            insert(Tree_1.root,myNode(n))
        inorder(Tree_1.root)

print(test())