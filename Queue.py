class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def print_queue(self):
        print(self.items)