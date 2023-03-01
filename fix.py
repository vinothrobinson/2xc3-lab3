import lab6

def fix(self, node):
    if node.parent is None:
        node.make_black()
        return
    while node is not None and node.parent is not None and node.parent.is_red():
        if node.is_right_child():
            node.rotate_left()
        elif node.is_left_child() and node.left.is_red():
            node.rotate_right()
        else:
            node = node.parent
    self.root.make_black()