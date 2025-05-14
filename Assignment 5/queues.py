# Using a list
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        # Add item to the end of the queue
        self.queue.append(item)

    def dequeue(self):
        # Remove item from the front of the queue if it's not empty
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Queue is empty")

    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):
        # Return the front item without removing it
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.queue)

# Usage
# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# print("Front element:", q.peek())    # Output: 1
# print("Dequeue element:", q.dequeue()) # Output: 1
# print("Is queue empty?", q.is_empty()) # Output: False
