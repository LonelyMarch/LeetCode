#!/usr/bin/env python
# coding=utf-8

'''
@Author: LonelyMarch
@LastEditors: LonelyMarch
@LastEditTime: 2021-02-21 17:54:07
@FilePath: /LeetCode/2021_02_18_《初级算法_实现strStr.py
@version:
@Descripttion:
'''


class Solution:
    # 滑动窗口
    @classmethod
    def strStr_SlidingWindow(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        right = len(needle)
        left = 0
        while right <= len(haystack):
            if haystack[left:right] == needle:
                return left
            left += 1
            right += 1
        return -1

    # 双指针
    @classmethod
    def strStr_DoublePointer(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        nlen = len(needle)
        hpoint = npoint = 0
        for hpoint in range(len(haystack)-nlen):
            if haystack[hpoint] == needle[npoint]:
                for i in range(nlen):
                    if haystack[hpoint+i] != needle[i]:
                        break
                if i == nlen-1:
                    return hpoint
        return -1


print("滑动窗口")
print(Solution.strStr_SlidingWindow(haystack="hello", needle="ll"))  # 2
print(Solution.strStr_SlidingWindow(haystack="abc", needle="c"))  # 2
print(Solution.strStr_SlidingWindow(haystack="ab", needle="c"))  # -1
print(Solution.strStr_SlidingWindow(haystack="ab", needle=""))  # 0
print(Solution.strStr_SlidingWindow(haystack="aaa", needle="aaaa"))  # -1
print(Solution.strStr_SlidingWindow(haystack="a", needle="a"))  # 0

print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")

print("双指针")
print(Solution.strStr_DoublePointer(haystack="hello", needle="ll"))  # 2
print(Solution.strStr_DoublePointer(haystack="abc", needle="c"))  # 2
print(Solution.strStr_DoublePointer(haystack="ab", needle="c"))  # -1
print(Solution.strStr_DoublePointer(haystack="ab", needle=""))  # 0
print(Solution.strStr_DoublePointer(haystack="aaa", needle="aaaa"))  # -1
print(Solution.strStr_DoublePointer(haystack="a", needle="a"))  # 0
