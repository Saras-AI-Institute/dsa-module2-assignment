from structures.static_array import StaticArray
from structures.dynamic_linked_list import DoublyLinkedList

class TelemetryBufferQueue:
    """
    Behavior Requirement: FIFO (First In, First Out)
    """
    def __init__(self):
        self.storage = DoublyLinkedList() 

    def enqueue_packet(self, packet: dict) -> None:
        """
        TODO: Add packet to the queue. 
        (Hint: You can insert at tail or head depending on your linked list implementation,
         just ensure FIFO order is maintained with dequeue!)
        """
        # YOUR CODE HERE
        pass

    def dequeue_packet(self) -> dict:
        """
        TODO: Remove and return the oldest packet.
        (Hint: Use self.storage.remove_from_tail() or equivalent method.)
        """
        # YOUR CODE HERE
        pass


class EmergencyOverrideStack:
    """
    Behavior Requirement: LIFO (Last In, First Out)
    Constraint: Memory is strictly limited to max_capacity slots.
    """
    def __init__(self, max_capacity=10):
        self.storage = StaticArray(max_capacity)
        self.top_index = -1
        self.max_capacity = max_capacity

    def push_critical_signal(self, error_code: str) -> None:
        """
        TODO: 
        1. Check if the stack is full (e.g., self.top_index + 1 >= self.max_capacity).
        2. If full, raise OverflowError("Stack Overflow: Max capacity exceeded").
        3. Otherwise, increment self.top_index and store in self.storage.set(self.top_index, error_code).
        """
        # YOUR CODE HERE
        pass

    def pop_critical_signal(self) -> str:
        """
        TODO: 
        1. Check if stack is empty (self.top_index < 0). If so, raise IndexError("Stack Underflow").
        2. Retrieve value using self.storage.get(self.top_index).
        3. Clear the slot by setting it to None: self.storage.set(self.top_index, None).
        4. Decrement self.top_index and return the value.
        """
        # YOUR CODE HERE
        pass
