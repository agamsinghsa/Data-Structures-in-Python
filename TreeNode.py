from Node import Node

class TreeNode(Node):
    def __init__(self, value, left=None, right=None):
        Node.__init__(self, value, right)
        self.left = left
