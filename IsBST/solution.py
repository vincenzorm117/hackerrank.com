#!/usr/local/bin/python3


class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.data)

def printStack(stack):
    print(' '.join(map(str, stack)))



def checkBSTRecursive(root):
    if type(root) != node:
        return False
    def cBST(curr, stack):
        # print(curr.data, stack)
        if curr is None:
            return True
        for n in stack:
            if n[1] == 1 and n[0].data < curr.data:
                return False
            if n[1] == -1 and n[0].data > curr.data:
                return False
        
        if curr.left is not None:
            leftStack = stack[:]
            leftStack.append((curr,1))
            left = cBST(curr.left, leftStack)
        else:
            left = True
        if curr.right is not None:
            rightStack = stack[:]
            rightStack.append((curr,-1))
            right = cBST(curr.right, rightStack)
        else:
            right = True
        return left and right
    return cBST(root, [])


def checkBSTRecursive2(root):
    if type(root) != node:
        return False
    def cBST(curr, stack):
        if curr is None:
            return True
        for n in stack:
            if n[1] == 1 and n[0].data < curr.data:
                return False
            if n[1] == -1 and n[0].data > curr.data:
                return False
        
        if curr.left is not None:
            stack.append((curr,1))
            left = cBST(curr.left, stack)
            stack.pop()
        else:
            left = True
        if curr.right is not None:
            stack.append((curr,-1))
            right = cBST(curr.right, stack)
            stack.pop()
        else:
            right = True
        return left and right
    return cBST(root, [])


def checkBST(root):
    if root is None:
        return True
    q = [(root, -10**100, 10**100)]
    while 0 < len(q):
        curr, min, max = q.pop()
        if curr.data < min or max < curr.data:
            return False
        if curr.left is not None:
            q.append((curr.left, min, curr.data-1))
        if curr.right is not None:
            q.append((curr.right, curr.data+1, max))
    return True
    

x = node(4)
x.left = node(2)
x.right = node(6)
x.left.left = node(1)
x.left.right = node(3)
x.right.left = node(5)
x.right.right = node(7)

print(checkBST(x))

# x = node(20)
# x.left = node(10)
# x.right = node(30)
# x.left.left = node(5)
# x.left.right = node(15)
# x.right.left = node(25)
# x.right.right = node(35)

# print(checkBST(x), checkBSTRecursive2(x))

# x = node(20)
# x.left = node(10)
# x.right = node(30)
# x.left.left = node(5)
# x.left.right = node(50)
# x.right.left = node(25)
# x.right.right = node(35)

# print(checkBST(x), checkBSTRecursive2(x))
