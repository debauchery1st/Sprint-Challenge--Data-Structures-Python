
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def enqueue(self, value):
        """
        add to head
        """
        if value:
            self.storage.insert(0, value)
            self.size += 1

    def dequeue(self):
        """
        remove from tail
        """
        if self.size > 0:
            self.size -= 1
            return self.storage.pop()


class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


if __name__ == "__main__":
    q = Queue()
