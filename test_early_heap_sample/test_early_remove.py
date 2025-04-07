import pytest
from heap_sample import Heaps

@pytest.mark.describe("Tests for the remove method in Heaps class")
class TestRemoveMethod:
    
    @pytest.mark.happy_path
    def test_remove_from_non_empty_heap(self):
        """
        Test removing the root element from a non-empty heap.
        The heap should re-heapify correctly after removal.
        """
        heap = Heaps()
        heap.heap = [1, 5, 10, 15, 20]
        removed_element = heap.remove()
        assert removed_element == 1
        assert heap.heap == [5, 15, 10, 20]  # Assuming a min-heap property

    @pytest.mark.happy_path
    def test_remove_single_element_heap(self):
        """
        Test removing the only element from a heap with a single element.
        The heap should be empty after removal.
        """
        heap = Heaps()
        heap.heap = [10]
        removed_element = heap.remove()
        assert removed_element == 10
        assert heap.heap == []

    @pytest.mark.edge_case
    def test_remove_from_empty_heap(self):
        """
        Test removing an element from an empty heap.
        The method should return None.
        """
        heap = Heaps()
        removed_element = heap.remove()
        assert removed_element is None
        assert heap.heap == []

    @pytest.mark.edge_case
    def test_remove_from_heap_with_duplicate_elements(self):
        """
        Test removing elements from a heap with duplicate values.
        The heap should maintain its properties after removal.
        """
        heap = Heaps()
        heap.heap = [1, 1, 1, 1, 1]
        removed_element = heap.remove()
        assert removed_element == 1
        assert heap.heap == [1, 1, 1, 1]  # Assuming a min-heap property

    @pytest.mark.edge_case
    def test_remove_from_heap_with_large_numbers(self):
        """
        Test removing elements from a heap with large numbers.
        The heap should maintain its properties after removal.
        """
        heap = Heaps()
        heap.heap = [1000000, 5000000, 10000000]
        removed_element = heap.remove()
        assert removed_element == 1000000
        assert heap.heap == [5000000, 10000000]  # Assuming a min-heap property

# Note: The `insert` and `display` methods are not defined in the provided code snippet.
# If they exist, they should be used to set up the heap state before tests.