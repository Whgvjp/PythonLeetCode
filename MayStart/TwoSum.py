# encoding: utf-8
#@Time : 2021/5/24 23:46
#@Auther : whgvjp
#@File : TwoSum.py

# class Solution:
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                else:
                    continue







