class DoubleStackQueue:
    # first in and first out
    def __init__(self):
        self.pushStack = []
        self.popStack = []

    def pushToPop(self):
        if not self.popStack:
            while self.pushStack:
                self.popStack.append(self.pushStack.pop())

    def push(self, num):
        self.pushStack.append(num)
        self.pushToPop()

    def pop(self):
        if not self.popStack and not self.pushStack:
            raise Exception("Stack is empty")
        self.pushToPop()
        return self.popStack.pop()

    def peek(self):
        if not self.popStack and not self.pushStack:
            raise Exception("Stack is empty")
        self.pushToPop()
        return self.popStack[-1]

