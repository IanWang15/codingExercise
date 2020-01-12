#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 23:39:57 2020

@author: yiwang
"""

# divided and conquer
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minimunTree(self, root: TreeNode):
        self.min = sys.maxsize
        self.minloc = None
        self.helper(root)
        return self.minimunTree
    
    def helper(self, root):
        results = []
        if root is None:
            return results# or just return, because it is return []
        left = self.helper(root.left)
        right = self.helper(root.right)
        results.append(root.val)
        if left:
            results.extend(left)
        if right:
            results.extend(right)
        localmin = sum(results)
        if localmin < self.min:
            self.min = localmin
            self.minimunTree = root.val
        return results
        
        
#[1,None,2,3]
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.left = TreeNode(0)
t.left.right = TreeNode(-2)
s = Solution()
t0 = s.minimunTree(t)
print(t0)
