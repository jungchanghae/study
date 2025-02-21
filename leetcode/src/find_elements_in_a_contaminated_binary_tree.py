# 1261. Find Elements in a Contaminated Binary Tree

"""
Given a binary tree with the following rules:

1. root.val == 0
2. For any treeNode:
    1. If treeNode.val has a value x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
    2. If treeNode.val has a value x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.

Implement the FindElements class:

FindElements(TreeNode* root) Initializes the object with a contaminated binary tree and recovers it.
bool find(int target) Returns true if the target value exists in the recovered binary tree.
"""

'''
모든 노드가 -1로 변한 이진 트리에서 주어진 숫자가 존재했는지를 찾아야하는 문제

0 1 2 3 4 ...로 흘러가지만,
null이 포함되는 순간 변화가 생기기 시작
모든 Tree를 복구하고, target이 존재하는지 살펴보자 -> set in을 이용해서 O(1)에 끝내기
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:
    def __init__(self, root: TreeNode):
        self.values = set()
        self.recover(root, 0)
        
    def recover(self, node, val):
        if not node:
            return
        node.val = val
        self.values.add(val)
        self.recover(node.left,2*val+1)
        self.recover(node.right,2*val+2)
        
    def find(self, target: int) -> bool:
        return target in self.values