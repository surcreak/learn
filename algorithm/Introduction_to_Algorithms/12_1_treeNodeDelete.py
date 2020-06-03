"""
Topic: 二叉搜索树删除节点
Desc :
    给定一个二叉搜索树，删除其中一个节点
"""

class Node:
    p = None
    left = None
    right = None
    key = None

    def __init__(self, key):
        self.key = key

"""
    数组转换为二叉搜索树。
    param a: 要转换的数组。
"""
def array2Tree(a):
    root = None
    for i in a:
        if root == None:
            root = Node(i)
        else:
            insetTree(root, i)
    return root

"""
    二叉搜索树插入数据。
    param root: 二叉搜索树的根。
    param input: 要插入的数据。
"""
def insetTree(root, input):
    node = Node(input)
    pointer = root
    while(pointer != None):
        if(pointer.key > input):
            if(pointer.left == None):
                node.p = pointer
                pointer.left = node
                break
            pointer = pointer.left
        else:
            if(pointer.right == None):
                node.p = pointer
                pointer.right = node
                break
            pointer = pointer.right
    return root

"""
    中序遍历二叉搜索树。
    param root: 二叉搜索树的根。
"""
def inOrderTraversalTree(root):
    if(root == None):
        return
    inOrderTraversalTree(root.left)
    print(root.key)
    inOrderTraversalTree(root.right)

"""
    查找二叉搜索树。
    param key: 要查找的key。
"""
def find(root, key):
    pointer = root
    while(pointer != None):
        if(pointer.key > key):
            pointer = pointer.left
        if(pointer.key < key):
            pointer = pointer.right
        else:
            break
    return pointer

"""
    删除二叉搜索树指定节点
    param T: 二叉搜索树的根节点
    param key: 要删除的key
"""
def nodeDelete(T, key):
    z = find(T, key)
    if(z == None or z == T):
        return None
    if(z.left == None):
        transplant(T, z, z.right)
    elif(z.right == None):
        transplant(T, z, z.left)
    else:
        y = treeNext(T, z.key)
        if y.p != z:
            transplant(T, y, y.right)
            y.right = z.right
            y.right.p = y
        transplant(T, z, y)
        y.left = z.left
        y.left.p = y

"""
    将二叉搜索树节点替换
    param T: 二叉搜索树的根节点
    param u: 被替换的子树
    param v: 替换用的子树
"""
def transplant(T, u, v):
    if(u.p == None):
        T = v
    elif(u == u.p.left):
        u.p.left = v
    elif(u == u.p.right):
        u.p.right = v
    if v != None:
        v.p = u.p

"""
    找到二叉搜索树的后继
    param T: 二叉搜索树的根节点
    param x: 当前节点
"""
def treeNext(T, x):
    y = find(T, x)
    z = y
    if (y == None):
        return None
    if (y.right != None):
        return treeMinimum(y.right)
    else:
        while(z.p.left == z):
            if z.p == None:
                break
            else:
                z = z.p
        return z

"""
    找到二叉搜索树的最小值
    param T: 二叉搜索树的根节点
"""
def treeMinimum(T):
    z = T
    while (z.left != None):
        z = z.left
    return z

if __name__ == '__main__':
    a = [5,3,6,2,4,7,12,32,43,45,29,9,3]
    root = array2Tree(a)
    inOrderTraversalTree(root)
    print("next:" +  repr(treeNext(root, 9).key))
    nodeDelete(root, 12)
    inOrderTraversalTree(root)