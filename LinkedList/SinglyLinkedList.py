class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertNodeSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode

        elif location == 0:  # Setting the new node at the start of the linked list
            newNode.next = self.head  # setting the current first node reference to the new node

            # setting the new node reference to the head or as the first element of the linked list
            self.head = newNode

        elif location == 1:  # Setting the new node at the end of the linked list
            newNode.next = None  # Setting the new lat node to none
            self.tail.next = newNode  # setting the reference of the newNode to the next variable of lastnode
            self.tail = newNode  # setting tail to newNode

        else:
            tempNode = self.head
            # Since CS we count from 0
            index = 0
            while index < location - 1:
                tempNode = tempNode.next
                index += 1
            nextNode = tempNode.next
            tempNode.next = newNode
            newNode.next = nextNode

    # Delete a node from Singly Linked List
    def deleteNodeSLL(self, location):
        if self.head is None:
            print("The SLL does not exit")
        elif location == 0:
            # To check if the SLL has only one node
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next

        elif location == 1:
            # To check if the SLL has only one node
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                node = self.head
                while node is not None:
                    # Checking if the node is the node before the last node
                    if node.next == self.tail:
                        break
                    node = node.next  # saving the last node a variable
                node.next = None  # Setting the last node to None
                self.tail = node
        else:
            tempNode = self.head
            index = 0
            while index < location - 1:
                tempNode = tempNode.next
                index += 1
            nextNode = tempNode.next
            tempNode.next = nextNode.next

    #Delete entire SLL
    def deleteEntireSLL(self):
        if self.head is None:
            print("The SLL does not exist")
        else:
            self.head = None
            self.tail = None



    # Traverse in Singly Linked List
    def traverseSLL(self):
        if self.head is None:
            print('This Singly Linked List does not exist')
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    # Search for a node in Singly Linked List
    def searchSLL(self, nodeValue):
        if self.head is None:
            return "This list does not exist"
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "The value does not exist in this list"


# singlyLinkedList = SLinkedList()
# node1 = Node(1)
# node2 = Node(2)
#
# singlyLinkedList.head = node1
# singlyLinkedList.head.next = node2
# singlyLinkedList.tail = node2

singlyLinkedList = SLinkedList()
singlyLinkedList.insertNodeSLL(1, 0)
singlyLinkedList.insertNodeSLL(2, 1)
singlyLinkedList.insertNodeSLL(3, 1)
singlyLinkedList.insertNodeSLL(4, 1)
singlyLinkedList.insertNodeSLL(5, 3)

print(list(node.value for node in singlyLinkedList))
singlyLinkedList.traverseSLL()
print("Value:", singlyLinkedList.searchSLL(3))

singlyLinkedList.deleteNodeSLL(2)
print(list(node.value for node in singlyLinkedList))


singlyLinkedList.deleteEntireSLL()
print(list(node.value for node in singlyLinkedList))


