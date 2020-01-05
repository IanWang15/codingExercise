#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 15:29:05 2020

@author: yiwang
"""
# traverse method

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode):
        self.results = []
        self.traverse(root)
        return self.results
    
    def traverse(self, node):
        if node is None:
            return
        self.results.append(node.val)
        self.traverse(node.left)
        self.traverse(node.right)

        
        
#[1,None,2,3]
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.left = TreeNode(4)
t.left.right = TreeNode(5)
s = Solution()
t0 = s.preorderTraversal(t)
print(t0)
