class Node:
    def __init__(self, value):
        self.data = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtBeginning(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insertAtEnd(self, value):
        new_node = Node(value)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def insertAtPosition(self, value, position):
        if position < 1:
            raise IndexError("Position must be >= 1")
        if position == 1:
            self.insertAtBeginning(value)
            return
        new_node = Node(value)
        current = self.head
        for _ in range(position - 2):
            if not current:
                raise IndexError("Position out of bounds")
            current = current.next
        if not current:
            raise IndexError("Position out of bounds")
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        if new_node.next is None:
            self.tail = new_node

    def deleteAtBeginning(self):
        if not self.head:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def deleteAtEnd(self):
        if not self.tail:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def deleteAtPosition(self, position):
        if position < 1:
            raise IndexError("Position must be >= 1")
        if not self.head:
            return
        if position == 1:
            self.deleteAtBeginning()
            return
        current = self.head
        for _ in range(position - 1):
            if not current:
                raise IndexError("Position out of bounds")
            current = current.next
        if not current:
            raise IndexError("Position out of bounds")
        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
        if current == self.tail:
            self.tail = current.prev

    def traverse(self):
        current = self.head
        if not current:
            print("The list is empty.")
            return
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        print("Length:", count)
        return count

    def get(self, position):
        if position < 1:
            raise IndexError("Position must be >= 1")
        current = self.head
        for _ in range(position - 1):
            if not current:
                raise IndexError("Position out of bounds")
            current = current.next
        if not current:
            raise IndexError("Position out of bounds")
        return current.data

    def find(self, value):
        current = self.head
        pos = 1
        while current:
            if current.data == value:
                return pos
            current = current.next
            pos += 1
        return -1

    def removeDuplicates(self):
        seen = set()
        current = self.head
        while current:
            if current.data in seen:
                next_node = current.next
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                current = next_node
            else:
                seen.add(current.data)
                current = current.next

dll = DoublyLinkedList()
dll.insertAtBeginning(10)
dll.insertAtBeginning(20)
dll.insertAtBeginning(30)
dll.insertAtEnd(40)
dll.insertAtEnd(50)
dll.insertAtPosition(25, 3)
print("List after insertions:")
dll.traverse()
dll.length()
print("Value at position 4:", dll.get(4))
print("Position of value 40:", dll.find(40))
dll.insertAtEnd(20)
dll.insertAtBeginning(10)
print("List before removing duplicates:")
dll.traverse()
dll.removeDuplicates()
print("List after removing duplicates:")
dll.traverse()
dll.deleteAtPosition(3)
print("List after deleting at position 3:")
dll.traverse()
dll.deleteAtBeginning()
print("List after deleting at beginning:")
dll.traverse()
dll.deleteAtEnd()
print("List after deleting at end:")
dll.traverse()