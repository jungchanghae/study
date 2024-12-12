"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
왼쪽부터 탐색하는 코드를 만들어야함
"""
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        self.Traveler(root, result)
        return result
    
    def Traveler(self,root,result):
        # 노드가 없으면 패스
        if root != None:
            self.Traveler(root.left,result)
            result.append(root.val)
            self.Traveler(root.right,result)