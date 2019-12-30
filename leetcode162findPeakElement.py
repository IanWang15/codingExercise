#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 00:35:56 2019

@author: yiwang
"""

class Solution():
    def findPeakElement(self, nums):
        if nums is None or len(nums) == 0:
            return -1
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = (end - start) // 2 + start
            if nums[mid] < nums[mid + 1]:
                start = mid
            else:
                end = mid
                
        if nums[start] < nums[end]:
            return end
        elif nums[start] > nums[end]:
            return start
        else:
            return -1

t = Solution()
t0 = t.findPeakElement([1,2,3,1])
print(t0)
                