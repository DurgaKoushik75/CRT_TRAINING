class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = new_node
            new_node.prev = pointer

    def insert_start(self, data):
        new_node = Node(data)
        temp = self.head
        self.head = new_node
        new_node.next = temp
        if temp:
            temp.prev = new_node

    def insert_middle(self, data, position):
        new_node = Node(data)
        pointer = self.head
        current = 1
        while current < position - 1 and pointer:
            pointer = pointer.next
            current += 1

        if pointer is None:
            return

        temp = pointer.next
        pointer.next = new_node
        new_node.prev = pointer
        new_node.next = temp

        if temp:
            temp.prev = new_node

    def delete_end(self):
        if self.head is None:
            return

        pointer = self.head
        while pointer.next:
            pointer = pointer.next

        if pointer.prev:
            pointer.prev.next = None
        else:
            self.head = None

    def delete_start(self):
        if self.head is None:
            return

        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def delete_middle(self, position):
        if self.head is None:
            return

        pointer = self.head
        current = 1
        while current < position and pointer:
            pointer = pointer.next
            current += 1

        if pointer is None or pointer.prev is None:
            return

        previous_pointer = pointer.prev
        next_pointer = pointer.next

        previous_pointer.next = next_pointer
        if next_pointer:
            next_pointer.prev = previous_pointer

    def traversal(self):
        pointer = self.head
        while pointer:
            print(pointer.data, end=" <-> ")
            pointer = pointer.next
        print()

dll = DoubleLinkedList()
dll.insert_end(10)
dll.insert_end(20)
dll.insert_end(30)
dll.insert_end(40)
dll.traversal()
dll.insert_start(50)
dll.traversal()
dll.insert_middle(60, 3)
dll.traversal()
dll.delete_middle(3)
dll.traversal()
