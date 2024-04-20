class QueueUsingStacks:
    def __init__(self):
        self.s1 = []  
        self.s2 = []  

    def is_empty(self):
        return len(self.s1) == 0

    def enqueue(self, data):
        self.s1.append(data)

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return

      

