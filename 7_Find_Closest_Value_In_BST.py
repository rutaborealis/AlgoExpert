'''
7. Find Closest Value In BST

Write a function that takes in a Binary Search Tree (BST) and a target integer
value and returns the closest value to that target value contained in the BST.

You can assume that there will only be one closest value.

Each BST node has an integer value, a left child node, and a right child node.

A node is said to be a valid BST node if and only if it satisfies the BST
property:
its value is strictly greater than the values of every node to its left;
its value is less than or equal to the values of every node to its right;
and its children nodes are either valid BST  nodes themselves or None / null.
'''

# 1
def findClosestValueInBst(tree, target):
    currentNode = tree
    closest = float('inf')

    while currentNode is not None:
        if abs(currentNode.value - target) < abs(closest - target):
            closest = currentNode.value

        if currentNode.value < target:
            currentNode = currentNode.right
            continue
        else:
            currentNode = currentNode.left

    return closest

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
