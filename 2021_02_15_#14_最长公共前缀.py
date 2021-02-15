#!/usr/bin/env python
# coding=utf-8

'''
@Author: LonelyMarch
@LastEditors: LonelyMarch
@LastEditTime: 2021-02-15 20:35:04
@FilePath: /LeetCode/2021_02_15_#14_最长公共前缀.py
@version:
@Descripttion:
'''


from typing import List


class Solution:
    @classmethod
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs in [[""], []]:
            return ""
        if len(strs) == 1:
            return strs[0]

        def CommonPrefix(a, b, k):
            result = ""
            x = 0
            while x < min(len(a), len(b)):
                if a[x] == b[x]:
                    result = result + a[x]
                    x += 1
                else:
                    break
            k += 1
            if k == len(strs):
                return result
            return CommonPrefix(result, strs[k], k)
        return CommonPrefix(strs[0], strs[1], 1)


# print(Solution.longestCommonPrefix(["dfad", "dfad", "dfadsd"]))
print(Solution.longestCommonPrefix(["a", ""]))
