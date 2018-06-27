class Node():
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
    def __str__(self):
        return str(self.value)

class LinkedList():
    def __init__(self):
        self.head = None
        self.curr = None
        self.last = None
    def insert(self, node, index=0):
        if self.head is None:
            self.head = node
            self.curr = self.head
        else:
            self.curr.next = node
            self.curr = self.curr.next
            node.next = self.last
        # self.head.next = self.last
    def traverse(self, index):
        node = self.head
        while node is not None and index is not 0:
            index-=1
            node = node.next
        return node
        

    def __str__(self):
        nodestr = ""
        node = self.head
        while node is not None:
            nodestr+=node
            node = node.next
        return nodestr

list = LinkedList()
list.insert(30)
list.insert(20)
print(list)
    