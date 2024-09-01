from typing import Optional

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
        print("")

    # On the right track, but the order is not correct
    def swapPairs(self, head: Optional[Node]) -> Optional[Node]:
        if head is None or head.next is None:
            return head

        first_node = head
        second_node = head.next

        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node

        return second_node



    def print_nodes(self):
        current_node = self.head
        while current_node:
            print(current_node)
            current_node = current_node.next

myList = LinkedList()

for i in range(1, 101):
    myList.insert(i)

myList.print_nodes()
myList.swapPairs(myList.head)
myList.print_list()
myList.print_nodes()

