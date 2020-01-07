#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 22:57:32 2020

@author: yiwang
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# divide & conquer
class Solution:
    def inorderTraversal(self, root: TreeNode):
        results = []
        if root is None:
            return results# or just return, because it is return []
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        
        results.extend(left)
        results.append(root.val)
        results.extend(right)
        return results
        
        
#[1,None,2,3]
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.left = TreeNode(4)
t.left.right = TreeNode(5)
s = Solution()
t0 = s.inorderTraversal(t)
print(t0)