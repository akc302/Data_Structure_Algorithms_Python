import Queue.QueueLinkedList as queue


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)

    return "The node has added successfully!"


##preOrder Traversal
def preOrderTraverse(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraverse(rootNode.leftChild)
    preOrderTraverse(rootNode.rightChild)


def inOrderTraverse(rootNode):
    if not rootNode:
        return
    else:
        inOrderTraverse(rootNode.leftChild)
        print(rootNode.data)
        inOrderTraverse(rootNode.rightChild)


def postOrderTraverse(rootNode):
    if not rootNode:
        return
    else:
        postOrderTraverse(rootNode.leftChild)
        postOrderTraverse(rootNode.rightChild)
        print(rootNode.data)


def levelOrderTraverse(
        rootNode):  # its too important! enque the node by left to right. Then dequeue it from the head of the linked list, after removing the head, connec the head with the second element of the linked list, !!
    if not rootNode:
        return
    else:  # i take python class from Queue, imported!
        cQ = queue.Queue()
        cQ.enqueue(rootNode)
        while not (cQ.isEmpty()):
            root = cQ.dequeue()
            print(root.value.data)  # understand that, here the value is the rootNode itself
            if root.value.leftChild is not None:
                cQ.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                cQ.enqueue(root.value.rightChild)


def searchNode(rootNode, value):
    if rootNode.data == value:
        # print("found")
        return 1
    elif value < rootNode.data:
        if rootNode.leftChild.data == value:
            print("found")
        else:
            searchNode(rootNode.leftChild, value)
    else:
        if rootNode.rightChild.data == value:
            print("found")
        else:
            searchNode(rootNode.rightChild, value)


# ================deleting node from BST================== important
# to find the successor (left most from right subtree, we need minValue func
def minValue(rootNode):
    current = rootNode
    while (current.leftChild is not None):
        current = current.leftChild
    return current


# this is interesting! if you try to delete the rootnode then you need to find the suceessor from right subtree. In the right sub tree, make the left most node the root node, and then delete the sucessor !
def deleteNode(rootNode, value):
    if rootNode is None:
        return
    if value < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, value)
    elif value > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, value)
    else:
        # if there is no left subtree then make the first node of right subtree rootnode.
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None  # making none cause delete the rootNode
            return temp
        # if there is no right subtree then make the first node of left subtree rootnode.
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None  # making none cause delete the rootNode
            return temp
        temp = minValue(rootNode.rightChild)  # to find the successor!!
        rootNode.data = temp.data  # temp.data has the successor data!
        # patience!
        # now we have to delete the successor data from right subtree
        # And, the successor data is in temp variable!
        # so, we again take help from Recusrion basic!
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)

    return rootNode


def deleteEntireBST(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "the BST deleted!"


newBST = BSTNode(None)
print(insertNode(newBST, 55))
print(insertNode(newBST, 70))
print(insertNode(newBST, 11))

print(newBST.data)
print(newBST.leftChild.data)
print(newBST.rightChild.data)

# levelOrderTraverse(newBST)
searchNode(newBST, 11)
deleteNode(newBST, 70)
levelOrderTraverse(newBST)  # checked the item 70 is deleted from BST!
print(deleteEntireBST(newBST))
