from structures.dynamic_linked_list import DoublyLinkedList

class KeyValuePair:
    def __init__(self, key: str, value: any):
        self.key = key
        self.value = value

class SensorRegistryHashTable:
    """
    A fixed-bucket Hash Table using Chaining for collision resolution.
    """
    def __init__(self, num_buckets: int = 10):
        self.num_buckets = num_buckets
        self.buckets = [DoublyLinkedList() for _ in range(num_buckets)]

    def _hash_function(self, key: str) -> int:
        """Simple deterministic hash function to map key to an index."""
        return sum(ord(char) for char in key) % self.num_buckets

    def put(self, key: str, value: any) -> None:
        """
        TODO: 
        1. Compute the bucket index: index = self._hash_function(key)
        2. Search the DoublyLinkedList at self.buckets[index] to see if the key exists.
           (Hint: Use bucket.search(lambda kv: kv.key == key))
        3. If the node/key exists, update its node.data.value = value.
        4. If it doesn't exist, create KeyValuePair(key, value) and insert at head:
           bucket.insert_at_head(KeyValuePair(key, value))
        """
        # YOUR CODE HERE
        pass

    def get(self, key: str) -> any:
        """
        TODO:
        1. Compute the bucket index.
        2. Search the linked list at that bucket for the key.
        3. Return node.data.value if found, otherwise raise KeyError("Key not found").
        """
        # YOUR CODE HERE
        pass
