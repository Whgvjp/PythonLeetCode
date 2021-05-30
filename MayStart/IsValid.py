# encoding: utf-8
#@Time : 2021/5/29 19:56
#@Auther : whgvjp
#@File : IsValid.py

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        while "()" in s or "{}" in s or "[]" in s:
            if "()" in s:
                s = s.replace("()","")
            if "[]" in s:
                s = s.replace("[]", "")
            if "{}" in s:
                s = s.replace("{}", "")
        return True if len(s) == 0 else False

if __name__ == '__main__':
    a = Solution
    print(a.isValid(a,"{(})[]"))


