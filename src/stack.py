# stack.py

class Stack:
    def __init__(self):
        self.items = []
        self.top = -1  # Pointer to the top of the stack

    def push(self, item):
        self.items.append(item)
        self.top += 1

    def pop(self):
        if not self.is_empty():
            top_item = self.items[self.top]
            #print(self.top)
            self.top -= 1
            #print(self.top)
            return top_item
            #self.top -= 1
            #print(self.top)
            #return self.items[self.top]
        else:
            return None

    def is_empty(self):
        return self.top == -1

    def peek(self):
        if not self.is_empty():
            return self.items[self.top]
        else:
            return None

    def size(self):
        return self.top + 1
