import pytest
from Binary_search_tree import Node

@pytest.mark.describe("Node.__init__")
class TestNodeInit:
    
    @pytest.mark.happy_path
    def test_node_initialization_with_valid_data(self):
        """
        Test that a Node is correctly initialized with valid data.
        """
        data = 10
        node = Node(data)
        assert node.data == data, "Node data should be initialized correctly"
        assert node.left is None, "Node left child should be initialized to None"
        assert node.right is None, "Node right child should be initialized to None"

    @pytest.mark.edge_case
    def test_node_initialization_with_none_data(self):
        """
        Test that a Node can be initialized with None as data.
        """
        data = None
        node = Node(data)
        assert node.data is None, "Node data should be initialized to None"
        assert node.left is None, "Node left child should be initialized to None"
        assert node.right is None, "Node right child should be initialized to None"

    @pytest.mark.edge_case
    def test_node_initialization_with_negative_data(self):
        """
        Test that a Node is correctly initialized with negative data.
        """
        data = -5
        node = Node(data)
        assert node.data == data, "Node data should be initialized correctly with negative value"
        assert node.left is None, "Node left child should be initialized to None"
        assert node.right is None, "Node right child should be initialized to None"

    @pytest.mark.edge_case
    def test_node_initialization_with_large_data(self):
        """
        Test that a Node is correctly initialized with a large integer.
        """
        data = 10**6
        node = Node(data)
        assert node.data == data, "Node data should be initialized correctly with large value"
        assert node.left is None, "Node left child should be initialized to None"
        assert node.right is None, "Node right child should be initialized to None"

    @pytest.mark.edge_case
    def test_node_initialization_with_string_data(self):
        """
        Test that a Node is correctly initialized with string data.
        """
        data = "test"
        node = Node(data)
        assert node.data == data, "Node data should be initialized correctly with string value"
        assert node.left is None, "Node left child should be initialized to None"
        assert node.right is None, "Node right child should be initialized to None"

    @pytest.mark.edge_case
    def test_node_initialization_with_float_data(self):
        """
        Test that a Node is correctly initialized with float data.
        """
        data = 3.14
        node = Node(data)
        assert node.data == data, "Node data should be initialized correctly with float value"
        assert node.left is None, "Node left child should be initialized to None"
        assert node.right is None, "Node right child should be initialized to None"

# To run the tests, use the command: pytest -v