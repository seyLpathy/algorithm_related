class ReverseStack:
    def __init__(self):
        self.stack=[]
    def reverse(self,stack):
        if not stack:
            return
        i = self.getAndRemoveLastElement(stack)
        self.reverse(stack)
        stack.append(i)


    def getAndRemoveLastElement(self,stack):
        result = stack.pop()
        if not stack:
            return result
        else:
            value = self.getAndRemoveLastElement(stack)
            stack.append(result)
            return value

