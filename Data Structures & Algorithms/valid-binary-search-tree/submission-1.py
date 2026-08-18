# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # DFS traversal with lower & upper bound
        def dfs(node, lower, upper):
            if node is None:
                return True
            
            if node.val <= lower or node.val >= upper:
                return False
            
            return dfs(node.left, lower, node.val) & dfs(node.right, node.val, upper)
        
        return dfs(root, float('-inf'), float('inf'))
        


# DFS traversal ---> partial correct
# check left -> check right
# if left, left < val; if right, right > val

