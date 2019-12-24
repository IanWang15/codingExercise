#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 01:44:53 2019

@author: yiwang
"""
import numpy as np

class Solution():
    def get(self, n):
        nums = np.arange(600)
        if n > len(nums):
            return 2147483647
        else:
            return nums[n]
    
    def searchBigSortedArray(self, target):
        if target < self.get(0):
            return -1
        
        n = 1
        while self.get(n) < target:
            n = n * 2
            
        start = 0
        end = n - 1
        while start + 1 < end:
            mid = (end - start) // 2 + start
            if target == self.get(mid):
                end = mid
            if target > self.get(mid):
                start = mid
            if target < self.get(mid):
                end = mid
        
        if start == target:
            return start
        if end == target:
            return end
        return -1
        
t = Solution()
print(t.searchBigSortedArray(10))