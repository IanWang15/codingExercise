#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 15:14:17 2019

@author: yiwang
"""

class Solution(object):
    def subsets(self, num):
        if num is None:
            return []
        result = [] # return a list of lists
        path   = [] # subsets
        self.dfs(result, path, num, 0)
        return result
    
    def dfs(self, result, path, num, pos):
        result.append(path.copy())
        # similarly as while loop, when pos > len(num)
        for i in range(pos, len(num)):
            path.append(num[i])
            # recursion
            self.dfs(result, path, num, i + 1)
            # backtracing
            path.pop(-1)
            
t = Solution()
t0 = t.subsets([1,2,3])
print(t0)
