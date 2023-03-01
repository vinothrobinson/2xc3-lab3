class Node:
        
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def is_leaf(self):
        return self.left is None and self.right is None

    def is_left_child(self):
        return self == self.parent.left

    def is_right_child(self):
        return not self.is_left_child()
    
    def __str__(self):
        return "(" + str(self.value) + ")"

    def __repr__(self):
        return "(" + str(self.value) + ")"

class BSTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def get_height(self):
        if self.is_empty():
            return 0
        return self.__get_height(self.root)

    def __get_height(self, node):
        if node is None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))