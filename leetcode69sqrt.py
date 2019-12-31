#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 23:12:32 2019

@author: yiwang
"""

class Solution():
    def findsqrt(self, x):
        start = 0
        end = x
        while (start + 1 < end):
            mid = (end - start) // 2 + start
            if mid**2 < x:
                start = mid
            elif mid**2 == x: # this is necessary
                start = mid
            else:
                end = mid
        if end**2 < x:
            return end
        else:
            return start
                
        
t = Solution()
t0 = t.findsqrt(9)
print(t0)


# Exponentiation is **, not ^
