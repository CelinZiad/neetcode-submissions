# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root

        while stack or node:

            # Go as far left as possible
            while node:
                stack.append(node)
                node = node.left

            # Go back to previous node
            node = stack.pop()

            # We just visited one node
            k -= 1

            if k == 0:
                return node.val

            # Now explore its right subtree
            node = node.right




        """
        LOGIC: DFS

        stack that keeps up history
        go to left node until none
        if len(stack)>k:
            need to go back to root and go right to k-len(stack)
        else:
            pop stack until reaching kth smallest value

        """