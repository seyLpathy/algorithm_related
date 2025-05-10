class RankStack:
    def __init__(self, stack):
        self.stack = stack

    def rank(self):
        help = []
        while self.stack:
            cur = self.stack.pop()
            while help and cur > help[-1]:
                self.stack.append(help.pop())
            help.append(cur)
        while help:
            self.stack.append(help.pop())
