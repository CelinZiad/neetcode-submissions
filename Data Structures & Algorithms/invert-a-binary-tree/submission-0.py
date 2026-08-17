# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        print(stack)
        while stack:
            node = stack.pop()
            if node == None:
                return None
            #print(node)
            temp = node.right
            node.right = node.left
            node.left = temp

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return root
