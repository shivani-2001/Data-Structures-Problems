# Question - https://leetcode.com/problems/permutation-in-string/

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1)

        s1 = Counter(s1)

        while right<=len(s2):
            if s1==Counter(s2[left:right]):
                return True
            left += 1
            right += 1

        return False