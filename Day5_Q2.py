# Question - https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        pre = []

        for i in s:
            if i in ["(", "[", "{"]:
                pre.append(i)
            else:
                if (len(pre) < 1):
                    return False
                elif (pairs[i] == pre[-1]):
                    pre.pop(-1)
                else:
                    return False

        if len(pre) != 0:
            return False
        else:
            return True