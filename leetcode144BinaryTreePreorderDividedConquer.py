#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 23:14:12 2020

@author: yiwang
"""

# divided and conquer
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode):
        results = []
        if root is None:
            return None
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        results.append(root.val)
        if left:
            results.extend(left)
        if right:
            results.extend(right)
        return results
        
#[1,None,2,3]
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.left = TreeNode(4)
t.left.right = TreeNode(5)
s = Solution()
t0 = s.preorderTraversal(t)
print(t0)
