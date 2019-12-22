#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 00:16:50 2019

@author: yiwang
"""

class solution(object):
    def firstTarget(self, nums, target):
        if nums is None or len(nums) == 0:
            return -1
        
        start = 0; end = len(nums) - 1
    # try not return during the while loop
    # [start ......... mid ............ end]
    
    # why not choosing start < end,
    # because to avoid corner case [2, 2] in searching last position of target
    
        while (start + 1 < end):
# it is ok write as mid = (start + end) / 2
# but, when adding two large numbers, may overflow
            mid = int((end - start) / 2) + start

            if target == nums[mid]:
                end = mid
            elif target < nums[mid]:
                end = mid
            else:
                # start = mid + 1 is also okay,
                # less than 1 iteration, but not easy to remember
                start = mid

#       double check
        if target == nums[start]:
            return start
        if target == nums[end]:
            return end
        return -1
        
t = solution()
t0 = t.firstTarget([5,7,7,8,8,10], 8)
print(t0)
t0 = t.firstTarget([5,7,7,8,8,10], 6)
print(t0)
                
# mistake:
# mess up "start" and "first" several times