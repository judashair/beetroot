from node import Node


class Queue:

    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    def append(self, item):
        temp = Node(item)

        if self.rear is None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def pop(self):
        if self.is_empty():
            return
        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.rear = None


q = Queue()
q.append(10)
q.append(20)
q.append(30)
q.pop()
q.append(50)
q.append(60)
q.append(70)
q.pop()
print("Queue Front " + str(q.front.data))
print("Queue Rear " + str(q.rear.data))
