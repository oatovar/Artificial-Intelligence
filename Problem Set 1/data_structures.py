class Queue:
    def __init__(self, list):
        self.queue = list()
        for item in list:
            self.insert(item)

    def empty(self):
        return len(self.queue) == 0
    
    def pop(self):
        if not self.empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty."

    def insert(self, item):
        if self.queue.append(item):
            return True
        else:
            return False

class Stack:
    def __init__(self):
        self.stack = list()

    def empty(self):
        return len(self.stack) == 0

    def pop(self):
        if not self.empty():
            return self.stack.pop()
        else:
            return "Stack is empty."
    
    def insert(self, item):
        if (self.stack.append(item)):
            return True
        else:
            return False
