class Node:
    def __init__(self, value):
        self.data = value
        self.pref = None

    def get_value(self):
        return self.data


class Stack:
    def __init__(self):
        self.end = None

    def push(self, item):
        if self.end is None:
            self.end = item
        else:
            item.pref = self.end
            self.end = item

    def pop(self):
        if self.end is None:
            raise Exception("Стек пуст")
        result = self.end
        self.end = result.pref
        result.pref = None
        return result.data

    def print(self):
        start = self.end
        while True:
            if start is not None:
                print(start.data)
                start = start.pref
            else:
                return
