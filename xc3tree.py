class XC3Node:
    def __init__(self, degree):
        self.degree = degree
        self.children = [None for _ in range(degree)]
        self.parent = None

    def is_leaf(self):
        return [child is None for child in self.children]

    def is_full(self):
        for child in self.children:
            if child is None:
                return False
            if not child.is_full():
                return False
        return True

    def insert(self):
        for i in range(len(self.children)):
            child = self.children[i]
            if child is None:
                if i > 1:
                    degree = i - 1
                else:
                    degree = 0
                self.children[i] = XC3Node(degree)
                self.children[i].parent = self
                return
            if not child.is_full():
                child.insert()
                return

    def increment_degree(self):
        self.degree += 1
        self.children.append(None)

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
