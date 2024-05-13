class QueueWithTwoStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def is_empty(self):
        return not self.stack1 and not self.stack2

queue = QueueWithTwoStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue peek:", queue.peek())  
print("Dequeue:", queue.dequeue())  
print("Queue peek:", queue.peek()) 
print("Dequeue:", queue.dequeue())  
print("Dequeue:", queue.dequeue())  
print("Dequeue:", queue.dequeue())  
