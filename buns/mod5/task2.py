class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None


class Queue:
    def __init__(self):
        self.start = None
        self.end = None

    def push(self, item):
        if self.start is None:
            self.end = item
            self.start = item
        else:
            self.end.nref = item
            item.pref = self.end
            self.end = item

    def pop(self):
        if self.start is not None:
            result = self.start
            self.start = self.start.nref
            return result.data
        else:
            raise Exception("Очередь пуста")

    def insert(self, index, item):
        if index < 0:
            raise IndexError

        current = self.start
        for i in range(index):
            if current is None:
                raise IndexError
            current = current.nref

        if current is None:
            item.pref = self.end
            self.end.nref = item
            self.end = item
            return

        if current.pref is not None:
            current.pref.nref = item
            item.pref = current.pref

        current.pref = item
        item.nref = current

        if current == self.start:
            self.start = item

    def print(self):
        current = self.start
        while True:
            if current is not None:
                print(current.data)
                current = current.nref
            else:
                return
