class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty")

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Stack:", stack.stack)

print("Peek:", stack.peek())

popped_item = stack.pop()
print("Popped item:", popped_item)
print("Stack after popping:", stack.stack)
