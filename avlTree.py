class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        self.height = 1
        self.parent = None


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


def height(node):
    if not node:
        return 0
    else:
        return node.height


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


def findNextRec(root):
    if root.left is None:
        return root
    root = findNextRec(root.left)
    return root

def findNextIter(curr):
    root = curr
    if root.right:
        root = root.right
        if root.left is None:
            return root
        while root.left != None:
            root = root.left
        return root
    else:
        if root.parent is None:
            return None
        else:
            if root.data > root.parent.data:
                return None
            else:
                return root.parent

def findPrevRec(root):
    if root.right is None:
        return root
    root = findPrevRec(root.right)
    return root

def findPrevIter(curr):
    root = curr
    if root.left:
        root = root.left
        if root.right is None:
            return root
        while root.right != None:
            root = root.right
        return root
    else:
        if root.parent is None:
            return None
        else:
            if root.data < root.parent.data:
                return None
            else:
                return root.parent

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

def deleteRec(root, number):
    if root is None:
        return root
    if number < root.data:
        root.left = deleteRec(root.left, number)
    elif number > root.data:
        root.right = deleteRec(root.right, number)
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
            temp = findPrevRec(root)
            root.data = temp.data
            root.left = deleteRec(root.left, temp.data)
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


def delIter(curr, number):
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
            temp = findPrevRec(root)
            root.data = temp.data
            number = temp.data
            p = root
            root = root.left
    balanceUp(p)
    while curr.parent:
        curr = curr.parent
    return curr


def insertRec(root, number):
    if not root:
        return newNode(number)
    elif number < root.data:
        root.left = insertRec(root.left, number)
    else:
        root.right = insertRec(root.right, number)

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


def insertIter(curr, number):
    if not curr:
        return newNode(number)
    changed = False
    parent = None
    root = curr
    while not changed:
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


def main():
    root = None
    root = insertIter(root, 5)
    root = insertIter(root, 2)
    root = insertIter(root, 8)
    root = insertIter(root, 1)
    root = insertIter(root, 3)
    root = insertIter(root, 7)
    root = insertIter(root, 10)
    root = insertIter(root, 4)
    root = insertIter(root, 6)
    root = insertIter(root, 9)
    root = insertIter(root, 11)
    root = insertIter(root, 12)
    

    displayNodes(root)
    root = delIter(root, 1)
    displayNodes(root)

    '''
    root = None
    root = insertRec(root, 20)
    root = insertRec(root, 4)
    root = insertRec(root, 26)
    root = insertRec(root, 3)
    root = insertRec(root, 9)
    root = insertRec(root, 21)
    root = insertRec(root, 30)
    root = insertRec(root, 2)
    root = insertRec(root, 7)
    root = insertRec(root, 11)
    displayNodes(root)
    root = insertRec(root, 8)
    displayNodes(root)


    root = None
    root = insertIter(root, 20)
    root = insertIter(root, 4)
    root = insertIter(root, 26)
    root = insertIter(root, 3)
    root = insertIter(root, 9)
    root = insertIter(root, 21)
    root = insertIter(root, 30)
    root = insertIter(root, 2)
    root = insertIter(root, 7)
    root = insertIter(root, 11)
    displayNodes(root)
    root = insertIter(root, 8)
    displayNodes(root)
    '''


if __name__ == "__main__":
    main()
