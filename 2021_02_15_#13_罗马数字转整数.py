#!/usr/bin/env python
# coding=utf-8

'''
@Author: LonelyMarch
@LastEditors: LonelyMarch
@LastEditTime: 2021-02-15 18:10:34
@FilePath: /LeetCode/2021_02_15_#13_罗马数字转整数.py
@version:
@Descripttion:
'''


class Solution:
    @classmethod
    def romanToInt(self, s: str) -> int:
        dct = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        numbfr = []
        c = 1
        numaft = 0
        for item in str(s):
            numbfr.append(item)
        while c < len(numbfr):
            if dct[numbfr[c-1]] < dct[numbfr[c]]:
                numaft -= dct[numbfr[c-1]]
            else:
                numaft += dct[numbfr[c-1]]
            c += 1
        numaft += dct[numbfr[-1]]
        return numaft


print(Solution.romanToInt("MCMXCIV"))


# def romanToInt(self, s: str) -> int:
#     a = 0
#     b = []
#     c = 1
#     d = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
#     for item in s:
#         b.append(item)
#     while c < len(b):
#         f = b[c-1:c+1]
#         e = d.get("".join(f))
#         if e:
#             a += e
#             b.pop(c-1)
#             b.pop(c-1)
#             continue
#         c += 1
#     for item in b:
#     a += b[item]
# return a
