class Node:
    """
    Node class to be used in the linked list implementation of the stack.
    """
    def __init__(self, data):
        """Initialize a node with data and a pointer to the next node."""
        self.data = data
        self.next = None

class CircularStack:
    """
    Circular stack class using a linked list with a maximum size of 5 elements.
    """
    MAX_SIZE = 5

    def __init__(self):
        """Initialize the stack with an empty state."""
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, distance):

        new_node = Node(distance)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head  # Circular link

        elif self.size < CircularStack.MAX_SIZE:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head  

        else:  # Stack is full, replace oldest
            self.head.data = distance
            self.head = self.head.next
            self.tail = self.tail.next  # Move tail 
        if self.size < CircularStack.MAX_SIZE:
            self.size += 1

    def pop(self):
        """Remove the oldest entry from the stack."""
        current = self.head
        if self.size == 0:
            raise IndexError("Circular stack is empty")

        if self.size == 1:
            self.head = None
            self.tail = None

        else:
            self.head = self.head.next  # Move head

        self.size -= 1


    def peek(self):
        """Get newest element from the stack."""
        if self.size == 0:
            raise IndexError("Circular stack is empty")
        return self.tail.data

    def print_stack(self):
        """Print all stored readings in order from oldest to newest."""
        if self.size == 0:
            print("Stack is empty")
            return

        current = self.head
        for _ in range(self.size):
            print(current.data)
            current = current.next



def is_empty(self):
        """Return True if the stack is empty, otherwise False."""
        return self.size == 0
