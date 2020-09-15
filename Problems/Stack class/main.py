class Stack():
    def __init__(self):
        self.my_stack = []

    def push(self, el):
        self.my_stack += [el]

    def pop(self):
        if self.is_empty():
            raise IndexError('List is empty')
        else:
            last = self.my_stack[-1]
            self.my_stack = self.my_stack[:self.my_stack.index(last)]
            return last

    def peek(self):
        if self.is_empty():
            raise IndexError('List is empty')
        else:
            return self.my_stack[-1]

    def is_empty(self):
        return not bool(self.my_stack)


