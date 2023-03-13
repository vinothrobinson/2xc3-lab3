class XC3Node:
    def __init__(self, degree):
        self.degree = degree
        if self.degree == 0:
            self.full = True
        else:
            self.full = False
        self.children = [None for _ in range(degree)]
        self.parent = None

    def is_leaf(self):
        return [child is None for child in self.children]

    def is_full(self):
        return self.full

    def update_full(self):
        for child in self.children:
            if child is None:
                return # Do not update value of full
            if not child.is_full():
                return False # Do not update value of full
        self.full = True
        if self.parent is not None:
            self.parent.update_full()
        return

    def insert(self):
        # Precondition: self.is_full returns False
        for i in range(len(self.children)):
            child = self.children[i]
            if child is None:
                if i > 1:
                    degree = i - 1
                else:
                    degree = 0
                self.children[i] = XC3Node(degree)
                self.children[i].parent = self
                self.update_full()
                return
            if not child.is_full():
                child.insert()

    def increment_degree(self):
        self.degree += 1
        self.children.append(None)
        self.update_full()

    def get_level(self):
        if self.parent is None:
            return 0
        return 1 + self.parent.get_level()

    def __str__(self):
        return "".join("\t" for _ in range(self.get_level())) + f"(#, {self.degree})"

    def __repr__(self):
        return str(self)


class XC3Tree:
    def __init__(self):
        self.root = None

    def get_degree(self):
        if self.root is None:
            return 0
        return self.root.degree

    def get_height(self):
        if self.root is None:
            return 0
        if self.root.degree == 0:
            return 1
        return 1 + max([self.__get_height(child) for child in self.root.children])

    def __get_height(self, node):
        if node is None:
            return 0
        if node.degree == 0:
            return 1
        return 1 + max([self.__get_height(child) for child in node.children])

    def get_size(self):
        if self.root is None:
            return 0
        size = 1
        for child in self.root.children:
            if child is not None:
                size += self.__get_size(child)
        return size

    def __get_size(self, node):
        if node is None:
            return 0
        size = 1
        for child in node.children:
            if child is not None:
                size += self.__get_size(child)
        return size

    def is_full(self):
        if self.root is None:
            return True
        return self.root.is_full()

    def insert(self):
        if self.root is None:
            self.root = XC3Node(0)
        else:
            if self.root.is_full():
                self.root.increment_degree()
            self.root.insert()

    def __str__(self):
        stack = [self.root]
        output = ""
        while stack != []:
            current_node = stack.pop()
            if current_node is not None:
                output += "\n" + str(current_node)
                for child in current_node.children[::-1]:
                    stack.append(child)
        return output

    def __repr__(self):
        return str(self)
