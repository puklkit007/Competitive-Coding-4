# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.flag = True
        def checkBalanced(root):
            if not root:
                return 0
            
            left = checkBalanced(root.left)
            right = checkBalanced(root.right)
            
            if abs(left - right) > 1:
                self.flag = False
                
            return 1 + max(left, right)
            
        checkBalanced(root)
        return self.flag
