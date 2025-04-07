import pytest
from Binary_search_tree import BST

@pytest.mark.describe("BST.append method")
class TestBSTAppend:
    
    @pytest.mark.happy_path
    def test_append_single_node(self):
        """Test appending a single node to an empty BST."""
        bst = BST()
        bst.append(10)
        assert bst.root is not None
        assert bst.root.data == 10

    @pytest.mark.happy_path
    def test_append_multiple_nodes(self):
        """Test appending multiple nodes to the BST."""
        bst = BST()
        bst.append(10)
        bst.append(5)
        bst.append(15)
        assert bst.root.data == 10
        assert bst.root.left.data == 5
        assert bst.root.right.data == 15

    @pytest.mark.happy_path
    def test_append_duplicate_nodes(self):
        """Test appending duplicate nodes to the BST."""
        bst = BST()
        bst.append(10)
        bst.append(10)
        assert bst.root.data == 10
        assert bst.root.left is None
        assert bst.root.right is None

    @pytest.mark.edge_case
    def test_append_to_empty_bst(self):
        """Test appending to an initially empty BST."""
        bst = BST()
        bst.append(20)
        assert bst.root is not None
        assert bst.root.data == 20

    @pytest.mark.edge_case
    def test_append_negative_values(self):
        """Test appending negative values to the BST."""
        bst = BST()
        bst.append(-10)
        bst.append(-20)
        bst.append(-5)
        assert bst.root.data == -10
        assert bst.root.left.data == -20
        assert bst.root.right.data == -5

    @pytest.mark.edge_case
    def test_append_large_values(self):
        """Test appending large values to the BST."""
        bst = BST()
        bst.append(1000000)
        bst.append(2000000)
        bst.append(500000)
        assert bst.root.data == 1000000
        assert bst.root.left.data == 500000
        assert bst.root.right.data == 2000000

    @pytest.mark.edge_case
    def test_append_minimum_integer(self):
        """Test appending the minimum integer value."""
        import sys
        bst = BST()
        bst.append(-sys.maxsize - 1)
        assert bst.root.data == -sys.maxsize - 1

    @pytest.mark.edge_case
    def test_append_maximum_integer(self):
        """Test appending the maximum integer value."""
        import sys
        bst = BST()
        bst.append(sys.maxsize)
        assert bst.root.data == sys.maxsize

# To run the tests, use the command: pytest -v