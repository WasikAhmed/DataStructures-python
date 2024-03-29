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

    def prepend(self, data):
        if not self.head:
            self.head = Node(data)
            return

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node.next:
            prev_node.next = Node(data)
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        if not self.head:
            return False

        if self.head.data == key:

            self.head = self.head.next
            return True

        current_node = self.head
        while current_node.next:
            if current_node.next.data == key:
                current_node.next = current_node.next.next
                return True
            current_node = current_node.next
        return False

    def delete_at_pos(self, pos):
        return

    def search(self, key):
        return

    def get_length(self):
        return

    def reverse(self):
        return

    def print_list(self):
        current_node = self.head

        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")
