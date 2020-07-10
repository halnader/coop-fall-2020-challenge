class Node:
    def __init__(self, data):
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
        self.last = node
        if self.first == None:
            self.first = node
        self.len += 1
        
class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.history = dLinkList()

    def add(self, num: int):
        self.history.appendNode(self.value)
        self.value += num
        pass

    def subtract(self, num: int):
        self.history.appendNode(self.value)
        self.value -= num
        pass

    def undo(self):
        self.history.appendNode(self.value)
        if self.history.last == None or self.history.last.prevN == None:
            print('Nothing to undo')
        else:
            self.value = self.history.last.prevN.data
        pass

    def redo(self):
        if self.history.last == None:
            print('Nothing to redo')
        else:
            self.value = self.history.last.data
        pass

    def bulk_undo(self, steps: int):
        for i in range(0, steps):
            self.undo
        pass

    def bulk_redo(self, steps: int):
        for i in range(0, steps):
            self.redo
        pass


    
