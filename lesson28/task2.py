from node import Node


class Stack:

    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            return popped_node.data

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.data

    def display(self):
        iter_node = self.head
        if self.is_empty():
            print("Stack Empty")
        else:
            while iter_node is not None:
                print(iter_node.data)
                iter_node = iter_node.next
            return


MyStack = Stack()

MyStack.push(10)
MyStack.push(20)
MyStack.push(30)
MyStack.display()
print("Fifo element is ", MyStack.peek())
MyStack.pop()
MyStack.pop()
MyStack.display()
print("Fifo element is ", MyStack.peek())
