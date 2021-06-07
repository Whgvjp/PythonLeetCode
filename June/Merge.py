# encoding: utf-8
#@Time : 2021/6/7 23:33
#@Auther : whgvjp
#@File : Merge.py

from typing import List
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    nums1[m:] = nums2
    nums1 = nums1.sort()
    