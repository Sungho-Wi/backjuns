class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()


if __name__ == "__main__":
    myStack = Stack()
    myStack.push('hello')
    myStack.push('world')

    print(myStack.pop())
    print(myStack.pop())
