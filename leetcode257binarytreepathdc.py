#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 23:08:43 2020

@author: yiwang
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
#  this is divide & conquer
#  results = [] is building somehow a subset,
#  and then add root.val for every path in that subset

class Solution:
    def binaryTreePath(self, root):
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [str(root.val)]
        left = self.binaryTreePath(root.left)
        right = self.binaryTreePath(root.right)
        
        results = []
        for path in left + right:
            results.append(str(root.val)+'->'+path)
        
        return results
            

    
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.left = TreeNode(4)
t.left.right = TreeNode(5)
s = Solution()
t0 = s.binaryTreePath(t)
print(t0)