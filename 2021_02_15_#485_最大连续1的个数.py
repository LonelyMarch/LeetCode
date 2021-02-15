#!/usr/bin/env python
# coding=utf-8

'''
@Author: LonelyMarch
@LastEditors: LonelyMarch
@LastEditTime: 2021-02-15 22:37:02
@FilePath: /LeetCode/2021_02_15_#485_最大连续1的个数.py
@version:
@Descripttion:
'''
from typing import List


class Solution:
    @classmethod
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return len(max("".join(str(val) for val in nums).split('0')))

    # def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    #     maxCount = count = 0
    #     for i, num in enumerate(nums):
    #         if num == 1:
    #             count += 1
    #         else:
    #             maxCount = max(maxCount, count)
    #             count = 0
    #     return max(maxCount, count)

    # def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    #     times = []
    #     for i in range(0, len(nums)):
    #         if nums[i] == 1:
    #             if nums[i-1] == 0 or i == 0:
    #                 time = 1
    #                 continue
    #             else:
    #                 time += 1
    #         else:
    #             try:
    #                 times.append(time)
    #             except:
    #                 pass
    #             time = 0
    #     times.append(time)
    #     return max(times)


print(Solution.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))
print(Solution.findMaxConsecutiveOnes([0, 0]))
