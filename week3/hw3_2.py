class binaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None
    
    root_val = preorder[0]
    root = binaryTree(root_val)

    index = inorder.index(root_val)

    root.left = buildTree(preorder[1:1+index], inorder[:index])
    root.right = buildTree(preorder[1+index:],inorder[index+1:])

    return root

def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))

preorder = list(map(int, input().split()))
inorder = list(map(int, input().split()))

root = buildTree(preorder, inorder)

print(height(root))