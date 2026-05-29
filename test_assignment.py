import pytest
from assignment import DynamicLinkedListStorage, select_linear_structure, DynamicQueue, CombinedCatalog

def test_linked_list_insertion():
    storage = DynamicLinkedListStorage()
    storage.insert_at_head("Data_A")
    storage.insert_at_head("Data_B")
    
    assert storage.size == 2
    assert storage.to_list() == ["Data_B", "Data_A"]

def test_linear_structure_selection():
    assert select_linear_structure('FAST_RANDOM_ACCESS') == 'ARRAY'
    assert select_linear_structure('DYNAMIC_GROWTH') == 'LINKED_LIST'
    assert select_linear_structure('MINIMIZE_MEM_FRAGMENTATION') == 'ARRAY'

def test_dynamic_queue_memory_scaling():
    dq = DynamicQueue(initial_capacity=2)
    dq.enqueue("Job1")
    dq.enqueue("Job2")
    assert dq.capacity == 2  # At capacity, but not exceeded yet
    
    dq.enqueue("Job3")
    assert dq.capacity == 4  # Triggers a dynamic resizing/doubling simulation

def test_combined_catalog_lookup():
    catalog = CombinedCatalog()
    catalog.register_item("Root/Documents", "resume.pdf")
    catalog.register_item("Root/Pictures", "vacation.png")
    
    assert catalog.get_category("resume.pdf") == "Root/Documents"
    assert catalog.get_category("vacation.png") == "Root/Pictures"
    assert catalog.get_category("non_existent.txt") is None
