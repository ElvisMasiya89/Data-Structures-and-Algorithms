class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

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
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        previous = self.head

        while temp.next:
            previous = temp
            temp = temp.next

        self.tail = previous
        self.tail.next = None
        self.length -= 1

        # if this no nodes left if the List then do this
        if self.length == 0:
            self.head = None
            self.tail = None

        # return removed node
        return temp.value

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True

    def pop_first(self):

        # if there are no  items in list
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        # This applies where there is one item in  the list
        if self.length == 0:
            self.tail = None

        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index > self.length - 1:
            return None
        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop()

        previous = self.get(index - 1)
        temp = previous.next
        previous.next = temp.next
        temp.next = None
        self.length = - 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        # introduce before and after nodes
        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


new_list = LinkedList(1)
new_list.append(2)
new_list.append(3)

# new_list.print_list()

# print(new_list.pop())
# print(new_list.pop())
# print(new_list.pop())


# new_list.prepend(10)
# new_list.print_list()
#
# new_list.pop_first()
# new_list.print_list()

# print(new_list.get(2))
#
# new_list.set(2, 5)

# new_list.insert(1, 3)

# print("temp:", new_list.remove(1))
new_list.reverse()
new_list.print_list()
