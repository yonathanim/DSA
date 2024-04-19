class LinearQueue:
    def __init__(self, max_size=10):
        self.queue = [None] * max_size
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return self.rear == self.max_size - 1

    def enqueue(self, data):
        if self.is_full():
            print("Queue Overflow")
        else:
            if self.front == -1:
                self.front = 0
            self.rear += 1
            self.queue[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
        else:
            data = self.queue[self.front]
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front += 1
            return data

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue elements: ", end=" ")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

# Example usage
queue = LinearQueue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()  # Output: Queue elements: 10 20 30
print(queue.dequeue())  # Output: 10
queue.display()  # Output: Queue elements: 20 30