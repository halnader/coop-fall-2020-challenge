class Node:
    def __init__(self, data: int):
        self.prevN = None
        self.nextN = None
        self.data = data
class dLinkList:
    def __init__(self):
        self.first = None
        self.last = None
        self.len = 0
    def appendNode(self, val):
        node = Node(val)
        node.prevN = self.last
        if self.last != None:
            self.last.nextN = node
        self.last = node
        if self.first == None:
            self.first = node
        self.len += 1
        
class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.history = dLinkList()
        self.history.appendNode(self.value)
        self.position = Node(0)

    def add(self, num: int):
        self.value += num
        self.history.appendNode(self.value)
        self.position = self.history.last
        pass

    def subtract(self, num: int):
        self.value -= num
        self.history.appendNode(self.value)
        self.position = self.history.last
        pass

    def undo(self):
        if self.position.prevN != None:
            self.position = self.position.prevN
        self.value = self.position.data
        pass

    def redo(self):
        if self.position.nextN != None:
            self.position = self.position.nextN
        self.value = self.position.data
        pass

    def bulk_undo(self, steps: int):
        for i in range(0, steps):
            self.undo()
        pass

    def bulk_redo(self, steps: int):
        for i in range(0, steps):
            self.redo()
        pass


    
