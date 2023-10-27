class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value


class Stack:
    def __init__(self):
        self.head = None

    def push(self, item):
        if self.head is None:
            self.head = item
        else:
            item.next = self.head
            self.head = item

    def pop(self):
        if self.head is None:
            raise Exception("Стек пуст")
        result = self.head
        self.head = result.next
        result.next = None
        return result.value

    def peek(self):
        return self.head.value

