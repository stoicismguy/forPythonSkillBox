class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class Queue:
    def __init__(self):
        self.tail = None
        self.head = None

    def enqueue(self, item):
        if self.tail is None:
            self.head = item
            self.tail = item
        else:
            self.tail.next = item
            self.tail = item

    def dequeue(self):
        if self.head is not None:
            result = self.head
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return result.value
        else:
            raise Exception("Очередь пуста")

