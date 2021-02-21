#!/usr/bin/env python
# coding=utf-8

'''
@Author: LonelyMarch
@LastEditors: LonelyMarch
@LastEditTime: 2021-02-21 17:47:34
@FilePath: /LeetCode/demo.py
@version: 
@Descripttion: 
'''


def strStr(haystack: str, needle: str) -> int:
    try:
        a = int(haystack.index(needle))
    except:
        a = -1
    return a


print(strStr(haystack="hello", needle="ll"))  # 2
print(strStr(haystack="abc", needle="c"))  # 2
print(strStr(haystack="ab", needle="c"))  # -1
print(strStr(haystack="ab", needle=""))  # 0
print(strStr(haystack="aaa", needle="aaaa"))  # -1
