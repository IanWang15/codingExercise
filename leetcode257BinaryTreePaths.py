#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 22:54:01 2020

@author: yiwang
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def binaryTreePath(self, root):
        if root is None:
            return
        results = []
        path = []
        self.helper(root, path, results)
        return results
        
    def helper(self, root, path, results):
        if not root:
            return
        path.append(str(root.val))
        if root.left is None and root.right is None:
            results.append('->'.join(path))#path.copy())
            path.pop()
            return
        
        self.helper(root.left, path, results)
        self.helper(root.right, path, results)
        path.pop()
        return

# this is traverse method with dps.
# I do not know why, this method does not be suggested 
# by jiuzhang website
    
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.left = TreeNode(4)
t.left.right = TreeNode(5)
s = Solution()
t0 = s.binaryTreePath(t)
print(t0)