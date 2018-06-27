class Node():
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.key)

class Tree():
    def __init__(self):
        self.root = None
    def print_inorder(self, root):
        if root:
            self.print_inorder(root.left)
            print(root)
            self.print_inorder(root.right)
    def insert(self, key):
        if(self.root is None):
            print("no root")
            self.root = Node(key)
        else:
            print("root exists")
            node = Node(key)
            self.insert_recursive(self.root, node)
    def insert_recursive(self, root, node):
        if(root.key<node.key):
            print("going right")
            if root.right is None:
                print("no right node")
                root.right = node
            else:
                print("going right again")
                self.insert_recursive(root.right, node)
        elif(root.key>node.key):
            print("going left")
            if root.left is None:
                print("no left node")
                root.left = node
            else:
                print("going left again")
                self.insert_recursive(root.left, node)
        else:
            print("root has the key already")
    def delete(self):

        pass

tree = Tree()
tree.insert(50)
tree.insert(4)
tree.insert(0)
tree.insert(5)
tree.insert(80)
tree.insert(555)
tree.print_inorder(tree.root)