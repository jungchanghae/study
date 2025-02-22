# 1028. Recover a Tree From Preorder Traversal

"""
We run a preorder depth-first search (DFS) on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

If a node has only one child, that child is guaranteed to be the left child.

Given the output traversal of this traversal, recover the tree and return its root.
"""

'''
'-'의 개수를 이용해 각 depth를 표시하고, 그걸 이용한다.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        for i in range(1000,0,-1):
            traversal = traversal.replace("-"*i,chr(i+65))
            
        node = self.recover_Tree(traversal, 1)
        return node
    
    def recover_Tree(self, remain_traversal, depth):
        remain_traversal = remain_traversal.split(chr(depth+65))
        node = TreeNode(int(remain_traversal[0]))
        node.left = self.recover_Tree(remain_traversal[1], depth+1) if len(remain_traversal) > 1 else None
        node.right = self.recover_Tree(remain_traversal[2], depth+1) if len(remain_traversal) > 2 else None
        return node
        
        

if __name__ == '__main__':
    sol = Solution()
    traversal = "1-2--3--4-5--6--7"
    
    print(sol.recoverFromPreorder(traversal))