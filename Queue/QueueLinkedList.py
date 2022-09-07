class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next


class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)

    def enqueue(self, value):
        newNode = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode

    def dequeue(self):
        if self.linkedList.head == None:
            return "There is no any node in the Q"
        else:
            tempNode = self.linkedList.head
            # check if there only one element by checking head== tail
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return tempNode

    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False


nQ = Queue()
nQ.enqueue(1)
nQ.enqueue(2)
nQ.enqueue(3)

print(nQ)
print(nQ.dequeue())
print(nQ)
print(nQ.isEmpty())
