#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 15:06:31 2019

@author: yiwang
"""

class Solution:
    def searchRange(self, nums, target: int):
        if nums is None or len(nums) == 0:
            return [-1, -1]
        first = self.firstPosition(nums, target)
        if first == -1:
            last = -1
        else:
            last  = self.lastPosition(nums[first:], target) + first
        return [first, last]
        
    def firstPosition(self, nums, target):
        start = 0
        end = len(nums) - 1
        
        while (start + 1 < end):
            mid = (end - start) // 2 + start
            if target == nums[mid]:
                end = mid
            elif target < nums[mid]:
                end = mid
            else:
                start = mid
                
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
    
    def lastPosition(self, nums, target):
        start = 0
        end = len(nums) - 1
        
        while (start + 1 < end):
            mid = int((end - start) / 2) + start
            if target == nums[mid]:
                start = mid
            elif target < nums[mid]:
                end = mid
            else:
                start = mid
                
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        return -1
    
t = Solution()
t0 = t.searchRange([5,7,7,8,8,10], 8)
print(t0)
t0 = t.searchRange([5,7,7,8,8,10], 6)
print(t0)
t0 = t.searchRange([], 0)
print(t0)

