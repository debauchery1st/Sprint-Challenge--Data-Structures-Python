

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.ring = []
        self.head = 0

    def append(self, item):
        if self.capacity == len(self.ring):
            self.ring.pop(self.head)  # remove oldest
            self.ring.insert(self.head, item)
            last = (self.capacity - 1)
            self.head = (self.head + 1) if (self.head < last) else 0
        else:
            self.ring.append(item)

    def get(self):
        return self.ring
