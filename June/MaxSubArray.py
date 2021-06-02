# encoding: utf-8
#@Time : 2021/6/2 23:05
#@Auther : whgvjp
#@File : MaxSubArray.py

from typing import List
def maxSubArray(nums: List[int]) -> int:
    num = 0
    maxArr = []
    for i in nums:
        num = num + i
        if num > 0:
            maxArr.append(num)
        else:
            maxArr.append(num)
            num = 0
    return max(maxArr) if len(maxArr) > 0 else 0


print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
