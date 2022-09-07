class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def enqueue(self, value):
        self.items.append(value)
        return "the element is added at the end of the queue"

    def dequeue(self):
        if self.items == []:
            return "nothing to dequue"
        else:
            self.items.pop(0)


cq = Queue()
print(cq.isEmpty())
cq.enqueue(2)
cq.enqueue(50)
print(cq)
cq.dequeue()
print(cq)
