class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def findPrevRec(root):
    if root.left is None:
        return root
    root = findPrevRec(root.left)
    return root


def findPrevIter(root):
    if root.left is None:
        return root
    while root.left != None:
        root = root.left
    return root


def findNextRec(root):
    if root.right is None:
        return root
    root = findNextRec(root.right)
    return root


def findNextIter(root):
    if root.right is None:
        return root
    while root.right != None:
        root = root.right
    return root


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
            temp = findNextRec(root.left)
            root.data = temp.data
            root.left = deleteRec(root.left, temp.data)

    return root


def delIter(curr, number):
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


def insertRec(root, number):
    if number < root.data:
        if root.left:
            insertRec(root.left, number)
        else:
            root.left = newNode(number)
    else:
        if root.right:
            insertRec(root.right, number)
        else:
            root.right = newNode(number)


def insertIter(root, number):
    changed = False
    while changed == False:
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


def findMinRec(root):
    return (findPrevRec(root.left).data)


def findMaxRec(root):
    return (findNextRec(root.right).data)


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

def bstToArr(root, a):
    if root:
        bstToArr(root.left,a)
        #print(root.data)
        a.append(root.data)
        bstToArr(root.right,a)
def sort(arr):
    root = newNode(arr[0])
    for i in range(1,len(arr)):
        insertRec(root, arr[i])
    a = []
    bstToArr(root, a)
    return a
def main():
    #Num 1 test
    '''
    root = newNode(10)
    insertIter(root, 5)
    insertIter(root, 17)
    insertIter(root, 18)
    insertIter(root, 14)
    insertIter(root, 16)
    displayNodes(root)
    print("\n")
    root = delIter(root, 18)
    displayNodes(root)

    
    insertRec(root, 5)
    insertRec(root, 17)
    insertRec(root, 18)
    insertRec(root, 14)
    insertRec(root, 16)

    displayNodes(root)
    print("\n")

    root = deleteRec(root, 17)
    displayNodes(root)
    print("\n")

    insertRec(root, 1)
    insertRec(root, 2)
    displayNodes(root)
    print("\n")

    print(findMinRec(root))
    print(findMaxRec(root))
'''

# Number 2 test
arr = [4,5,6,1,2,3]
print(sort(arr))


if __name__ == "__main__":
    main()
