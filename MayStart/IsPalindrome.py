# encoding: utf-8
#@Time : 2021/5/26 22:15
#@Auther : whgvjp
#@File : IsPalindrome.py
# 判断是否是回文数字

class Solution:
    def isPalindrome(self, x: int) -> bool:
        intstr = str(x)
        if x<0:
            return False
        elif intstr == intstr[::-1]:
            return True
        else:
            return False

if __name__ == '__main__':
    so = Solution
    print(so.isPalindrome(so,121))