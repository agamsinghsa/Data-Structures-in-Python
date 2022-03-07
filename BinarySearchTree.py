from TreeNode import TreeNode

class BinarySearchTree(TreeNode):
    def __init__(self, value, left=None, right=None):
        TreeNode.__init__(self, value, left, right)
        
    def insert(self, value):
        current_node = self
        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = TreeNode(value)
                    break
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = TreeNode(value)
                    break
                else:
                    current_node = current_node.right
        return self
        
    def remove(self, value, parent_node = None):
        current_node = self
        while current_node is not None:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            else:
                if current_node.left is not None and current_node.right is not None:
                    current_node.value = current_node.right.get_min_value()
                    current_node.right.remove(current_node.value, current_node)
                elif parent_node is None: # this is the case where we don't have a parent_node
                    if current_node.left is not None:
                        current_node.value = current_node.left.value
                        current_node.right = current_node.left.right
                        current_node.left = current_node.left.left
                    elif current_node.right is not None:
                        current_node.value = current_node.right.value
                        current_node.left = current_node.right.left
                        current_node.right = current_node.right.right
                    else:
                        pass # we have just the one node that contains our value
                elif parent_node.left == current_node:
                    parent_node.left = current_node.left if current_node.left else current_node.right
                elif parent_node.right == current_node:
                    parent_node.right = current_node.left if current_node.left else current_node.right
                break
        return self
    
    def get_min_value(self):
        current_node = self
        while current_node.left:
            current_node = current_node.left
        return current_node.value
    
    def contains(self, value):
        current_node = self
        while current_node:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            else:
                return True
        return False
