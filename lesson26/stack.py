class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[len(self._items) -1]

    def size(self):
        return len(self._items)

    def __repr__(self):
        representation = "Reversed input:\n"
        for item in reversed(self._items):
            representation += f"{str(item)}"
        return representation

    def __str__(self):
        return self.__repr__()


# s = Stack()
#
# print(s.is_empty())
# s.push(4)
# s.push('dog')
# print(s.peek())
# s.push(True)
# print(s.size())
# print(s.is_empty())
# s.push(8.4)
# print(s.pop())
# print(s.pop())
# print(s.size())
# print(s)
# print(s.pop())
# print(s)