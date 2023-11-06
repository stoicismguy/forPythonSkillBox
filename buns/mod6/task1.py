class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.start = None
        self.iter_now = None

    def __iter__(self):
        current = self.start
        while current is not None:
            yield current.data
            current = current.next

    def push(self, item):
        if self.start is None:
            self.start = item
            self.iter_now = self.start
        else:
            current = self.start
            while True:
                if current is not None:
                    if current.next is None:
                        current.next = item
                        break
                    else:
                        current = current.next

    def remove(self, index):
        current = self.start
        prev = current
        for _ in range(index):
            if current is not None:
                if current.next is not None:
                    prev = current
                    current = current.next
                else:
                    raise IndexError()

        if current == self.start:
            if current.next is not None:
                self.start = current.next
            else:
                self.start = None
        else:
            if current.next is not None:
                prev.next = current.next
            else:
                prev.next = None

    def insert(self, index, item):
        current = self.start
        prev = current
        for _ in range(index):
            if current is not None:
                if current.next is not None:
                    prev = current
                    current = current.next
                else:
                    raise IndexError()

        if index != 0:
            item.next = current
            prev.next = item
        else:
            if self.start is not None:
                item.next = self.start
                self.start = item

    def get(self, index):
        current = self.start
        for _ in range(index):
            if current is not None:
                if current.next is not None:
                    current = current.next
                else:
                    raise IndexError()
        return current.data

    def print(self):
        current = self.start
        while True:
            if current is not None:
                print(current.data)
                current = current.next
            else:
                return
