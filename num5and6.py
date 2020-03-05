import random
import sys
countAVL = countBST = 0

class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        self.height = 1
        self.parent = None

def height(node):
    if not node:
        return 0
    else:
        return node.height

def findNextRec(root):
    if root.left is None:
        return root
    root = findNextRec(root.left)
    return root

def findNextIter(root):
    if root.right is None:
        return root
    while root.right != None:
        root = root.right
    return root

def findPrevRec(root):
    if root.right is None:
        return root
    root = findPrevRec(root.right)
    return root

def findPrevIter(root):
    if root.left is None:
        return root
    while root.left != None:
        root = root.left
    return root

def findMinRec(root):
    if root.right is None:
        return root
    root = findPrevRec(root.right)
    return root.data


def findMinIter(root):
    if root.left is None:
        return root
    while root.left != None:
        root = root.left
    return root.data


def findMaxRec(root):
    if root.right is None:
        return root
    root = findPrevRec(root.right)
    return root.data

def findMaxIter(root):
    if root.right is None:
        return root
    while root.right != None:
        root = root.right
    return root.data


def displayNodes(root):
    queue = []
    queue.append(root)
    while len(queue) > 0:
        print(queue[0].data)
        temp_node = queue.pop(0)
        if temp_node.left is not None:
            queue.append(temp_node.left)
        if temp_node.right is not None:
            queue.append(temp_node.right)
    print("\n")

##################################################################

def BalanceFactor(root):
    left = height(root.left)
    right = height(root.right)
    return left - right


def balanceUp(curr):
    node = curr
    while node:
        node.height = 1 + max(height(node.left), height(node.right))
        bf = BalanceFactor(node)
        if abs(bf) > 1:
            if bf > 1:  # bf = 2
                if BalanceFactor(node.left) >= 0:  # height(node.left.left) > height(node.left.right):
                    RightRotate(node)
                    # return RightRotate(node)
                    # LL case
                else:
                    node.left = LeftRotate(node.left)
                    node = RightRotate(node)
                    # return RightRotate(node)
                    # LR case
            else:
                if BalanceFactor(node.right) <= 0:  # height(node.right.right > height(node.right.left)):
                    LeftRotate(node)
                    # return LeftRotate(node)
                    # RR case
                else:
                    node.right = RightRotate(node.right)
                    node = LeftRotate(node)
                    # return LeftRotate(node)
                    # RL case
        else:
            node = node.parent
    return node


def RightRotate(node):
    p = node.parent

    a = node.left
    b = node.left.right
    node.left = None
    a.right = node

    a.parent = p
    if p:
        if node.data < p.data:
            p.left = a
        else:
            p.right = a
    node.parent = a
    node.left = b

    node.height = 1 + max(height(node.left), height(node.right))
    a.height = 1 + max(height(a.left), height(a.right))
    return a


def LeftRotate(curr):
    node = curr
    p = node.parent

    a = node.right
    b = node.right.left
    node.right = None
    a.left = node

    a.parent = p
    if p:
        if node.data < p.data:
            p.left = a  #
        else:
            p.right = a
    node.parent = a
    node.right = b

    node.height = 1 + max(height(node.left), height(node.right))
    a.height = 1 + max(height(a.left), height(a.right))
    return a



def deleteRecAVL(root, number):
    if root is None:
        return root
    if number < root.data:
        root.left = deleteRecAVL(root.left, number)
    elif number > root.data:
        root.right = deleteRecAVL(root.right, number)
    else:
        if root.left is None and root.right is None:
            root = None
            return root
        elif root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        else:
            temp = findPrevRec(root.left)
            root.data = temp.data
            root.left = deleteRecAVL(root.left, temp.data)
    root.height = 1 + max(height(root.left), height(root.right))
    bf = BalanceFactor(root)
    node = root
    if abs(bf) > 1:
        if bf > 1:  # bf = 2
            if BalanceFactor(node.left) >= 0:
                return RightRotate(node)
                # LL case
            else:
                node.left = LeftRotate(node.left)
                return RightRotate(node)
                # LR case
        else:
            if BalanceFactor(node.right) <= 0:
                return LeftRotate(node)
                # RR case
            else:
                node.right = RightRotate(node.right)
                return LeftRotate(node)
                # RL case
    else:
        return root


def delIterAVL(curr, number):
    root = curr
    done = False
    while not done:
        found = False
        while not found:
            if number < root.data:
                root = root.left
            elif number > root.data:
                root = root.right
            else:
                found = True

        p = root.parent
        if root.left is None and root.right is None:
            if root.data <= p.data:
                p.left = None
            else:
                p.right = None
            root = None
            done = True
        elif root.left is None:
            if root.data < p.data:
                p.left = root.right
            else:
                p.right = root.right
            root = None
            done = True
        elif root.right is None:
            if root.data < p.data:
                p.left = root.left
            else:
                p.right = root.left
            root = None
            done = True
        else:
            temp = findPrevRec(root.left)
            root.data = temp.data
            number = temp.data
            p = root
            root = root.left
    balanceUp(p)
    while curr.parent:
        curr = curr.parent
    return curr


def insertRecAVL(root, number):
    if not root:
        return newNode(number)
    elif number < root.data:
        root.left = insertRecAVL(root.left, number)
    else:
        root.right = insertRecAVL(root.right, number)

    root.height = 1 + max(height(root.left), height(root.right))

    # balance factor
    left_tree = height(root.left)
    right_tree = height(root.right)
    bf = left_tree - right_tree

    node = root
    if abs(bf) > 1:
        if bf > 1:  # bf = 2
            if BalanceFactor(node.left) >= 0:  # height(node.left.left) > height(node.left.right):
                return RightRotate(node)
                # LL case
            else:
                node.left = LeftRotate(node.left)
                return RightRotate(node)
                # LR case
        else:
            if BalanceFactor(node.right) <= 0:  # height(node.right.right > height(node.right.left)):
                return LeftRotate(node)
                # RR case
            else:
                node.right = RightRotate(node.right)
                return LeftRotate(node)
                # RL case
    else:
        return root


def insertIterAVL(curr, number):
    global countAVL
    if not curr:
        return newNode(number)
    changed = False
    parent = None
    root = curr
    
    while not changed:
        countAVL += 1
        if number < root.data:
            if root.left:
                parent = root
                root = root.left
            else:
                root.left = newNode(number)
                parent = root
                root = root.left
                root.parent = parent
                changed = True
        else:
            if number > root.data:
                if root.right:
                    root = root.right
                else:
                    root.right = newNode(number)
                    parent = root
                    root = root.right
                    root.parent = parent
                    changed = True
    balanceUp(root.parent)

    while curr.parent:
        curr = curr.parent
    return curr


###################################################################

def deleteRecBST(root, number):
    if root is None:
        return root
    if number < root.data:
        root.left = deleteRecBST(root.left, number)
    elif number > root.data:
        root.right = deleteRecBST(root.right, number)

    else:
        if root.left is None and root.right is None:
            root = None
            return root
        elif root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        else:
            temp = findNextRec(root.left)
            root.data = temp.data
            root.left = deleteRecBST(root.left, temp.data)

    return root

def delIterBST(curr, number):
    parent = None
    root = curr
    done = False
    while done == False:
        found = False
        while found == False:
            if number < root.data:
                parent = root
                root = root.left
            elif number > root.data:
                parent = root
                root = root.right
            else:
                found = True

        if root.left is None and root.right is None:
            if root.data <= parent.data:
                parent.left = None
            else:
                parent.right = None
            root = None
            done = True
        elif root.left is None:
            if root.data < parent.data:
                parent.left = root.right
            else:
                parent.right = root.right
            root = None
            done = True
        elif root.right is None:
            if root.data < parent.data:
                parent.left = root.left
            else:
                parent.right = root.left
            root = None
            done = True
        else:
            temp = findNextIter(root.left)
            root.data = temp.data
            number = temp.data
            parent = root
            root = root.left
    return curr

def insertRecBST(root, number):
    if number < root.data:
        if root.left:
            insertRecBST(root.left, number)
        else:
            root.left = newNode(number)
    else:
        if root.right:
            insertRecBST(root.right, number)
        else:
            root.right = newNode(number)
    
def insertIterBST(root, number):
    global countBST
    changed = False
    while changed == False:
        countBST += 1
        if number < root.data:
            if root.left:
                root = root.left
            else:
                root.left = newNode(number)
                changed = True
        else:
            if number > root.data:
                if root.right:
                    root = root.right
                else:
                    root.right = newNode(number)
                    changed = True

def bstToArr(root, a):
    if root:
        bstToArr(root.left,a)
        #print(root.data)
        a.append(root.data)
        bstToArr(root.right,a)


   # *****************************************************************************************
def getRandomArray(n):
    dicts = {}
    arr = []
    for i in range(n):
        a = True
        while a:
            val = random.randint(-sys.maxsize - 1, sys.maxsize)
            ans = dicts.get(val, "no")
            if ans == "no":
                dicts[val] = 1
                a = False
        arr.append(val)
    return arr
       
def getSortedArray(n):
    arr = []
    for i in range(n,0,-1):
        arr.append(i)
    return arr

def main():
  
    nums = getRandomArray(10000)
    nums2 = getSortedArray(10000)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    
    root1 = None
    for i in range(10000):
        root1 = insertIterAVL(root1, nums[i])
    print("num levels in AVL is "+ str(countAVL))
    root2 = newNode(nums[0])
    for i in range(1, 10000):
        insertIterBST(root2, nums[i])
    print("num levels in BST is "+ str(countBST))
    
    '''
    root1 = None
    for i in range(10000):
        root1 = insertIterAVL(root1, nums2[i])
    print("num levels in AVL is "+ str(countAVL))
    root2 = newNode(nums2[0])
    for i in range(1, 10000):
        insertIterBST(root2, nums2[i])
    print("num levels in BST is "+ str(countBST))
    '''

if __name__ == "__main__":
    main()


