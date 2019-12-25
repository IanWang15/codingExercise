#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 19:02:50 2019

@author: yiwang
"""

class Solution:
    def findmin(self, nums):
        if nums is None or len(nums) == 0:
            return -1
        
        start = 0
        end = len(nums) - 1
        while (start + 1 < end):
            mid = (end - start) // 2 + start
            if nums[mid] == nums[-1]:
                end = mid
            if nums[mid] < nums[-1]:
                end = mid
            if nums[mid] > nums[-1]:
                start = mid
        
        print(start,end)
        if nums[start] <= nums[-1]:
            return nums[start]
        if nums[end] <= nums[-1]:
            return nums[end]
        return -1#num[0]
    
t = Solution()
n = t.findmin([2,4,7,9,0])
print(n)

n = t.findmin([0])
print(n)

# error log
# line 26 and 28 should use <=, should not use < only
