#!/usr/bin/env python
# coding=utf-8

'''
@Author: LonelyMarch
@LastEditors: LonelyMarch
@LastEditTime: 2021-02-15 13:27:51
@FilePath: /LeetCode/2021_02_14_#1_两数之和.py
@version: 
@Descripttion: 
'''


from typing import List


class Solution:
    @classmethod
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = 1
        for a in nums:
            nums_b = nums[x:]
            for b in nums_b:
                if a+b == target:
                    return nums.index(a), nums_b.index(b)+x
            x += 1


print(Solution.twoSum([2, 3, 4], 6))
