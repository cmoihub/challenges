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
        # self.last = None
    def insert(self, value, index=0):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            if index is 0:
                node.next = self.head
                self.head = node
            else:
                self.curr = self.traverse(index)
                node.next = self.curr.next
                self.curr.next = node

    def traverse(self, index):
        node = self.head
        while node.next is not None and index is not 0:
            index-=1
            node = node.next
        return node
    def __str__(self):
        nodestr = ""
        node = self.head
        count = 1
        while node is not None:
            nodestr+=" " + (str(count)) + "."
            nodestr+=node.__str__()
            count+=1
            node = node.next
        
        return nodestr

list = LinkedList()
list.insert(30)
list.insert(20)
list.insert(40,1)
list.insert(50)
list.insert(2,2)
list.insert(60, 90)

print(list)