#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 21:48:01 2020

@author: yiwang
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
#  this is traverse method
# results here are actually global variable

class Solution:
    def binaryTreePath(self, root):
        results = []
        if root is None:
            return results
        self.helper(root,str(root.val),results)
        return results
        
    def helper(self, root, path, results):
        if root is None:
            return
        if root.left is None and root.right is None:
            results.append(path)
            return

        if root.left:
            self.helper(root.left, path+'->'+str(root.left.val), results)
        if root.right:
            self.helper(root.right, path+'->'+str(root.right.val), results)
        return

    
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.left = TreeNode(4)
t.left.right = TreeNode(5)
s = Solution()
t0 = s.binaryTreePath(t)
print(t0)