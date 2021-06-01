# encoding: utf-8
#@Time : 2021/6/1 23:06
#@Auther : whgvjp
#@File : SearchInsert.py
# 输入: [1,3,5,6], 5
# 输出: 2
# 输入是有序的

from typing import List
# class Solution:
def searchInsert(nums: List[int], target: int) -> int:
    res = 0
    for i in nums:
        if i<target:
            res += 1
        else:
            break
    return res

print(searchInsert([1,3,4,6],5))