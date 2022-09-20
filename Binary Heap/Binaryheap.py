class Heap:
    def __init__(self, size):
        self.customList = (size + 1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1


def levelOrder(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1, rootNode.heapSize + 1):
            print(rootNode.customList[i])


def heapify(rootNode, index, heapType):
    parentIndex = int(index / 2)
    if index <= 1:
        return
    if heapType == "min":
        if rootNode.customList[parentIndex] > rootNode.customList[index]:
            temp = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = rootNode.customList[index]
            rootNode.customList[index] = temp

    if heapType == "max":
        if rootNode.customList[parentIndex] < rootNode.customList[index]:
            temp = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = rootNode.customList[index]
            rootNode.customList[index] = temp
    heapify(rootNode, parentIndex, heapType)


def insertNode(rootNode, nodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "full"
    else:
        rootNode.customList[rootNode.heapSize + 1] = nodeValue
        rootNode.heapSize += 1
        heapify(rootNode, rootNode.heapSize, heapType)


newHeap = Heap(5)
insertNode(newHeap, 5, "min")
insertNode(newHeap, 3, "min")
insertNode(newHeap, 11, "min")
insertNode(newHeap, 1, "min")
levelOrder(newHeap)
