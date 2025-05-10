class Stack1:
    def __init__(self):
        self.data = []
        self.min = []

    def push(self, newNum):
        if not self.min:
            self.min.append(newNum)
        elif newNum < self.getMin():
            self.min.append(newNum)
        self.data.append(newNum)

    def pop(self):
        if not self.data:
            raise IndexError('Stack is empty')
        value = self.data.pop()
        if value == self.getMin():
            self.min.pop()
        return value

    def getMin(self):
        if not self.min:
            raise IndexError('Stack is empty')
        return self.min[-1]

