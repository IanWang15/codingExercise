#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 23:52:57 2020

@author: yiwang
"""

# traverse
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# divide & conquer
class Solution:
    def inorderTraversal(self, root: TreeNode):
        if root is None:
            return
        results = []
        self.helper(root, results)
        return results
    
    def helper(self, root, results):
        if not root:
            return
        self.helper(root.left, results)
        results.append(root.val)
        self.helper(root.right, results)
        return
        
        
#[1,None,2,3]
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.left = TreeNode(4)
t.left.right = TreeNode(5)
s = Solution()
t0 = s.inorderTraversal(t)
print(t0)