class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        val = self.list.reverse()
        val = [str(x) for x in self.list]
        return ' '.join(val)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    def push(self, value):
        if self.isFull():
            return "the stack is full"
        else:
            self.list.append(value)
            return "the element is successfully added"


cS = Stack(4)
print(cS.isEmpty())
print(cS.isFull())
cS.push(11)
cS.push(12)
cS.push(13)
print(cS)
