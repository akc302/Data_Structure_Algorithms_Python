import Queue.QueueLinkedList as queue


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


newBT = TreeNode("Drinks")  # o(1)
leftChild = TreeNode("Hot")  # o(1)
rightChild = TreeNode("Colds")  # o(1)
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild = coffee
leftChild.rightChild = tea
newBT.leftChild = leftChild
newBT.rightChild = rightChild


# pre-order Traverse


def preOrderTraversal(rootNode):  # o(n)
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)  # O(n/2)
    preOrderTraversal(rootNode.rightChild)  # O(n/2)


# preOrderTraversal(newBT)

# inOrder traversal in a binary Tree


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)


# we can do the Post Order!
# left node - right node - root

# level Order Binary Tree
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQ = queue.Queue()
        customQ.enqueue(rootNode)
        while not (customQ.isEmpty()):
            root = customQ.dequeue()
            print(root.value.data)  # value is a node
            if (root.value.leftChild is not None):
                customQ.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQ.enqueue(root.value.rightChild)


# delete binary tree, if we can delete the head then garbage collector will collect rest of the nodes

def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "deleted"


deleteBT(newBT)
levelOrderTraversal(newBT)
