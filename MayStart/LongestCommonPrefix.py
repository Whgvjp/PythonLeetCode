# encoding: utf-8
#@Time : 2021/5/28 22:52
#@Auther : whgvjp
#@File : LongestCommonPrefix.py

from typing import List
# ['flower', 'aflow', 'dflight']
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        llen = len(strs)
        cstr = strs[0]
        for i in range(1,llen):
            cstr = self.coPrefix(cstr,strs[i])
        return cstr

    @classmethod
    def coPrefix(self,str1: str,str2: str):
        mlen = min(len(str1),len(str2))
        index = 0
        #下面这个and前后不能反过来，如果反过来可能出现最小长度是0，然后str1[0]取不到而报错
        while index < mlen and str1[index] == str2[index]:
            index += 1
        return str1[:index]

#
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""
#
#         prefix, count = strs[0], len(strs)
#         for i in range(1, count):
#             prefix = self.lcp(prefix, strs[i])
#             if not prefix:
#                 break
#
#         return prefix
#
#     @classmethod
#     def lcp(self, str1, str2):
#         length, index = min(len(str1), len(str2)), 0
#         while index < length and str1[index] == str2[index]:
#             index += 1
#         return str1[:index]



if __name__ == '__main__':
    so = Solution
    print(so.longestCommonPrefix(so,['flower', 'aflow', 'dflight']))

