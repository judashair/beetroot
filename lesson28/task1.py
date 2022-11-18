from node import Node


class UnorderedList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def append(self, item):
        if self._head is None:
            self._head = Node(item)
        else:
            new_node = Node(item)
            new_node.next = self._head
            self._head = new_node

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def index(self, item):
        pass

    def pop(self, item):
        current = self._head
        previous = None
        found = False
        while not found:

            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())
