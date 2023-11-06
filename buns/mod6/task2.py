class DoubleElement:
    def __init__(self, *lst):
        self.data = lst
        self.pointer = 0

    def __next__(self):
        if len(self.data) == 0 or self.pointer >= len(self.data):
            raise StopIteration

        first_item = self.data[self.pointer]
        self.pointer += 1
        second_item = None
        if self.pointer < len(self.data):
            second_item = self.data[self.pointer]
        self.pointer += 1
        result = [first_item, second_item]
        return result

    def __iter__(self):
        return self
