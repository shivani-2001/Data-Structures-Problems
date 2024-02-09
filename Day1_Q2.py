"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Method 1 ->
        count = {}
        count1 = {}

        for i in s:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        for i in t:
            if i in count1:
                count1[i] += 1
            else:
                count1[i] = 1

        if count == count1:
            return True
        else:
            return False


        # Method 2 ->
        """if len(s) != len(t):
            return False
        for i in s:
            if s.count(i) != t.count(i):
                return False

        return True"""


        # Method 3 ->
        """if sorted(s) == sorted(t):
            return True
        else:
            return False"""