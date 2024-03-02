# Question - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s1 = ""
        left, right = 0, 0
        count = 0

        while right<len(s):
            if s[right] in s1:
                s1 = ""
                left += 1
                right = left
            else:
                s1 += s[right]
                count = max(count, (right-left+1))
                right += 1
                
        return count