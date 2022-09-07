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


newBST = BSTNode(None)
print(insertNode(newBST, 55))
print(insertNode(newBST, 70))
print(insertNode(newBST, 11))

print(newBST.data)
print(newBST.leftChild.data)
print(newBST.rightChild.data)

levelOrderTraverse(newBST)
