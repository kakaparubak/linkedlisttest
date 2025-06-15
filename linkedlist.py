# The building blocks of the LL (Linked List)
class Node():
    def __init__(self, value, next_node=None) -> None:
        self.value = value
        self.next = next_node


# Linked list itself
class LinkedList():
    def __init__(self, head=None) -> None:
        self.head = head

    # Inserts a node at the beginning of the LL
    def insert_beginning(self, value=None):
        node = Node(value, self.head)
        self.head = node
        return

    # Inserts a node at the end of the LL
    def insert_end(self, value=None):
        if self.head == None:
            node = Node(value)
            self.head = node
            return

        itr = self.head
        while itr:
            if itr.next is None:
                node = Node(value)
                itr.next = node
                return

            else:
                itr = itr.next

    # Inserts a node anywhere the LL
    def insert(self, index, value=None):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index.")

        if index == 0:
            self.insert_beginning(value)
            return

        itr = self.head
        node = Node(value)
        for i in range(index - 1):
            itr = itr.next

        node.next = itr.next
        itr.next = node
        return

    # Inserts a node after another node containing a specified value
    def insert_after_value(self, fixed_value, new_value):
        node = Node(new_value)
        itr = self.head
        while itr:
            if itr.value == fixed_value:
                node.next = itr.next
                itr.next = node
                return
            else:
                itr = itr.next

    # Inserts a list into the end of the LL
    def insert_list(self, values):
        for value in values:
            self.insert_end(value)

    # Outputs the length of the LL
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1

        return count

    # Removes the last node of the LL
    def remove_end(self):
        itr = self.head
        nextnode = itr.next
        while itr:
            if nextnode.next is None:
                itr.next = None
                return
            else:
                itr = nextnode
                nextnode = itr.next

    # Removes the first node of the LL
    def remove_beginning(self):
        self.head = self.head.next

    # Removes a node of the LL by an index
    def remove(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index.")

        if index == 0:
            self.remove_beginning()
            return

        itr = self.head
        for i in range(index - 1):
            itr = itr.next

        placeholder = itr.next
        itr.next = placeholder.next

    # Removes a node of the LL by a value
    def remove_by_value(self, value):
        if self.head.value == value:
            self.head = self.head.next

        itr = self.head
        nextitr = itr.next
        while itr.next is not None:
            if nextitr.value == value:
                itr.next = nextitr.next
                nextitr.next = None
                return

            itr = nextitr
            nextitr = itr.next

    # Edits a node's value at the specified index
    def edit_value(self, index, value):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index.")

        itr = self.head
        for i in range(index):
            itr = itr.next

        itr.value = value

    # Finds a node's index by it's value
    def find(self, value):
        itr = self.head
        index = 0

        while itr:
            if itr.value == value:
                return index

            index += 1
            itr = itr.next

        return -1

    # Outputs the whole LL to a string
    def output(self):
        itr = self.head
        llstring = ''

        if self.head == None:
            return 'This linked list is empty.'
        while itr:
            llstring += f'{itr.value} -> '
            itr = itr.next

        return llstring
