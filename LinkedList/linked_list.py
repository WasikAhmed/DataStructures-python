class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def print_list(self):
        current_node = self.head

        while current_node.next:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")


