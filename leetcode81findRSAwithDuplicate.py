#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 19:19:06 2019

@author: yiwang
"""
class Solution():
    def findTargetRSA(self, nums, target):
        if nums is None or len(nums) == 0:
            return False
        start = 0
        end   = len(nums) - 1
        
        if nums[start] == nums[end]:
            if len(nums) == 1:
                if target == nums[0]:
                    return True#nums[0]
                else:
                    return False
            while ((start + 1 < len(nums) - 1) and \
                   (nums[start] == nums[start + 1])):
                start = start + 1
            start = start + 1
        
        while (start + 1 < end):
            mid = (end - start) // 2 + start
            # mid 2 < target < end; pure binary search
            if target >= nums[mid] and target <= nums[end]:
                start = mid
            # start < target < mid 1; pure binary search
            elif target >= nums[start] and target <= nums[mid]:
                end = mid
            # target > mid 1; continue to find peak in RSA
            elif nums[mid] >= nums[start]:
                start = mid
            # target < mid 2; continue to find peak in RSA
            else:
                end = mid
        if target == nums[end]:
            return True#end
        if target == nums[start]:
            return True#start
        return False
    
    
t = Solution()
t0 = t.findTargetRSA([4,5,6,7,0,1,2], 0)
print(t0)

t0 = t.findTargetRSA([1], 0)
print(t0)

t0 = t.findTargetRSA([1,3], 1)
print(t0)