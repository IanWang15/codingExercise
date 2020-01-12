#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 00:14:00 2020

@author: yiwang
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def balanceTree(self, root: TreeNode):
        layer, isbalance = self.helper(root)
        return isbalance

    def helper(self, root):
        if root is None:
            return 0, True
        leftlayer, leftisbalance = self.helper(root.left)
        rightlayer, rightisbalance = self.helper(root.right)
        leftlayer = leftlayer + 1
        rightlayer = rightlayer + 1
        if not leftisbalance:
            return leftlayer, False
        if not rightisbalance:
            return rightlayer, False
        if abs(leftlayer - rightlayer) > 1:
            return rightlayer, False

        return max(leftlayer, rightlayer), True
        
        
#[1,None,2,3]
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.left = TreeNode(0)
t.left.right = TreeNode(-2)
s = Solution()
t0 = s.balanceTree(t)
print(t0)