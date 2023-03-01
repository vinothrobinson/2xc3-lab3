class RBNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.colour = "R"

    def is_leaf(self):
        return self.left is None and self.right is None

    def is_left_child(self):
        return self == self.parent.left

    def is_right_child(self):
        return not self.is_left_child()

    def is_red(self):
        return self.colour == "R"

    def is_black(self):
        return not self.is_red()

    def make_black(self):
        self.colour = "B"

    def make_red(self):
        self.colour = "R"

    def get_brother(self):
        if self.parent.right == self:
            return self.parent.left
        return self.parent.right

    def get_uncle(self):
        return self.parent.get_brother()

    def uncle_is_black(self):
        if self.get_uncle() is None:
            return True
        return self.get_uncle().is_black()

    def __str__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    def __repr__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    def rotate_right(self):
        # Setting temp variables for pointers
        temp_colour = self.parent.colour
        s_r = self.right
        s_p_p = self.parent.parent
        right_child = self.parent.is_right_child()

        # Re-arranging pointers for rotating right
        self.right = self.parent
        self.parent.parent = self
        self.parent = s_p_p
        if self.parent.parent is not None:
            if right_child:
                s_p_p.right = self
            else:
                s_p_p.left = self
        self.right.left = s_r
        if self.right is not None:
            self.right.left.parent = self.right

        # Fixing colours of rotated nodes
        self.colour = temp_colour
        self.right.make_red()

    def rotate_left(self):
        left = self.parent
        middle = self.left
        top = left.parent

        # Fix pointers to and from top
        self.parent = top
        if top is not None:
            if left.is_right_child():
                top.right = self
            else:
                top.left = self

        left.parent = self
        left.right = middle

        # Fix pointers to and from left and middle
        if middle is not None:
            middle.parent = left
        self.left = left

        # Fix colours
        self.colour = left.colour
        left.make_red()


class RBTree:

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

    def insert(self, value):
        if self.is_empty():
            self.root = RBNode(value)
            self.root.make_black()
        else:
            self.__insert(self.root, value)

    def __insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = RBNode(value)
                node.left.parent = node
                self.fix(node.left)
            else:
                self.__insert(node.left, value)
        else:
            if node.right is None:
                node.right = RBNode(value)
                node.right.parent = node
                self.fix(node.right)
            else:
                self.__insert(node.right, value)

    def fix(self, node):
        #You may alter code in this method if you wish, it's merely a guide.
        if node.parent is None:
            node.make_black()
        while node is not None and node.parent is not None and node.parent.is_red():
            pass
            #TODO
        self.root.make_black()

    def __str__(self):
        if self.is_empty():
            return "[]"
        return "[" + self.__str_helper(self.root) + "]"

    def __str_helper(self, node):
        if node.is_leaf():
            return "[" + str(node) + "]"
        if node.left is None:
            return "[" + str(node) + " -> " + self.__str_helper(node.right) + "]"
        if node.right is None:
            return "[" + self.__str_helper(node.left) + " <- " + str(node) + "]"
        return "[" + self.__str_helper(node.left) + " <- " + str(node) + " -> " + self.__str_helper(node.right) + "]"


T = RBTree()
T.insert(10)
T.insert(20)
print(T)
T.root.right.rotate_left()
T.root = T.root.parent
print(T)

print()

T = RBTree()
T.insert(100)
T.insert(200)
T.insert(10)
T.insert(20)
print(T)
T.root.left.right.rotate_left()
print(T)