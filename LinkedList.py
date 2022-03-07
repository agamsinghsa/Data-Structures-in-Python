from Node import Node

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.right:
                current_node = current_node.right
            current_node.right = Node(value)
        return self
        
    def remove(self, value):
        if self.head.value == value:
            self.head = self.head.right
        else:
            parent = self.head
            current_node = self.head.right
            while current_node:
                if current_node.value == value:
                    parent.right = current_node.right
                current_node = current_node.right
                parent = parent.right
        return self
      
    def to_string(self):
        current_node = self.head
        while current_node:
            print(current_node.value, "-> ", end="")
            current_node = current_node.right
        print("None")
        return self
