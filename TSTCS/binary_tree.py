class BinaryTree:
    def __init__(self,value):
        self.key = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.left_child = self.left_child
            self.left_child = bin_tree
        
    def insert_right(self, value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.right_child = self.right_child
            self.right_child = bin_tree
    
    # Breadth first search method
    def breadth_first_search(self, n):
        current = [self]
        next = []

        while current:
            for node in current:
                if node.key == n:
                    return True
                if node.left_child:
                    next.append(node.left_child)
                if node.right_child:
                    next.append(node.right_child)
            
            current = next
            next = []
        return false
    
    # Binary tree inversion 
    def invert(self):
        current = [self]
        next = []

        while current:
            for node in current:
                if node.left_child:
                    next.append(node.left_child)
                if node.right_child:
                    next.append(node.right_child)
                
                tmp = node.left_child
                node.left_child = node.right_child
                node.right_child = tmp
            
            current = next
            next = []


# Preorder, postorder and inorder traversal methods
def preorder(tree):
    if tree:
        print(tree.key)
        preorder(tree.left_child)
        preorder(tree.right_child)

def postorder(tree):
    if tree:
        postorder(tree.left_child)
        postorder(tree.right_child)
        print(tree.key)
        
def inorder(tree):
    if tree:
        inorder(tree.left_child)
        print(tree.key)
        inorder(tree.right_child)


# building a tree and testing the methods

tree = BinaryTree(1)
tree.insert_left(2)
tree.insert_right(3)
tree.insert_left(4)
tree.left_child.insert_right(6)
tree.insert_right(5)

print(tree.left_child.key)

print(tree.breadth_first_search(4))

preorder(tree)
print()
postorder(tree)
print()
inorder(tree)

