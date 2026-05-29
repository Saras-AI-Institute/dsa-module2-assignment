"""
Module 2 Assignment: Selecting Data Structures (Performance & Memory Constraints)
Fill in the blanks/complete the classes and functions below according to the docstrings.
"""

from typing import List, Any, Optional

# =====================================================================
# SECTION 1: Linear Selection & Memory Constraints (Array vs. Linked List)
# =====================================================================

class Node:
    """A standard Node for a Singly Linked List implementation."""
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional['Node'] = None


class DynamicLinkedListStorage:
    """
    A dynamic storage structure optimized to conserve memory by expanding 
    only when elements are added (unlike a static array).
    """
    def __init__(self):
        self.head: Optional[Node] = None
        self.size = 0

    def insert_at_head(self, data: Any) -> None:
        """
        Task 1a: Insert data at the beginning of the linked list.
        Time Complexity: O(1)
        """
        # TODO: Implement this method
        pass

    def to_list(self) -> List[Any]:
        """Helper method to convert the linked list to a standard Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result


def select_linear_structure(constraint: str) -> str:
    """
    Task 1b: Theoretical Scenario Analyzer.
    Return 'ARRAY' or 'LINKED_LIST' based on the dominant architectural constraint.
    
    Constraints:
    - 'FAST_RANDOM_ACCESS': You need to access elements instantly via an index in O(1) time.
    - 'MINIMIZE_MEM_FRAGMENTATION': You need contiguous memory blocks for hardware caching.
    - 'DYNAMIC_GROWTH': You have highly unpredictable data volume and strict memory limits; 
                        you cannot afford large pre-allocated empty spaces.
    """
    # TODO: Evaluate the constraint string and return either 'ARRAY' or 'LINKED_LIST'
    pass


# =====================================================================
# SECTION 2: Dynamic & Non-Linear Selection (Hash Tables, Queues, & Trees)
# =====================================================================

class DynamicQueue:
    """
    A simple simulation of a dynamic queue tracking its capacity and size,
    demonstrating how dynamic data structures manage memory thresholds.
    """
    def __init__(self, initial_capacity: int = 4):
        self.capacity = initial_capacity
        self.queue_items: List[Any] = []

    def enqueue(self, item: Any) -> None:
        """
        Task 2: Simulate enqueueing an item. If the number of items reaches capacity,
        simulate a dynamic memory reallocation by doubling the capacity.
        """
        # TODO: Implement this method
        pass


class CombinedCatalog:
    """
    Task 3: Combining Data Structures.
    To optimize access time and track hierarchies, combine a Hash Map and a Tree.
    
    We simulate a simple directory path look-up system using:
    1. A Python dictionary (Hash Table) for O(1) instant lookup.
    2. A nested hierarchy structure representing a non-linear tree layout.
    """
    def __init__(self):
        # A hash map to instantly map a key to its data
        self.lookup_table = {}

    def register_item(self, category: str, item_name: str) -> None:
        """
        Store items such that they are categorized by a structural directory.
        The lookup_table should map the item_name (key) to its category (value).
        """
        # TODO: Implement this method
        pass

    def get_category(self, item_name: str) -> Optional[str]:
        """Return the category of the item in O(1) time using the hash map."""
        # TODO: Implement this method
        pass
