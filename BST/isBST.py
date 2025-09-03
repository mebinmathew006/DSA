class Solution:
    def isBST(self, node, minValue=float('-inf'), maxValue=float('inf')):
        if not node:
            return True  # Empty tree is a valid BST
        
        # Check if node's value is within the allowed range
        if node.value <= minValue or node.value >= maxValue:
            return False
        
        # Recursively check left and right subtrees with updated constraints
        return (self.isBST(node.left, minValue, node.value) and
                self.isBST(node.right, node.value, maxValue))
