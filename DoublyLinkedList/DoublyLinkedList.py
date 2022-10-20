class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1
        return True

    def pop(self):
        if self.head is None:
            return None

        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp

        else:
            temp = self.tail
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None
            self.length -= 1
            return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1
        return True

    def pop_first(self):
        if self.head is None:
            return None

        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
            self.length -= 1
            return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        elif index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp

        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
            return temp


new_list = DoublyLinkedList(5)
new_list.append(6)
new_list.append(7)
# new_list.pop()
# new_list.prepend(4)
# new_list.pop_first()
print(new_list.get(1).value)
# new_list.print_list()
