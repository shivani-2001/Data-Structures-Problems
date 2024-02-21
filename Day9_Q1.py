# Question - https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Method 1 ->
        s = [i for i in s if i.isalnum()]
        s = "".join(s).lower()
        for i in range(len(s)//2):
            if s[i]!=s[-(i+1)]:
                return False

        return True

        # Method 2 ->
        new = ''
        for a in s:
            if a.isalpha() or a.isdigit():
                new += a.lower()
        return (new == new[::-1])