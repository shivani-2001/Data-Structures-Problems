# Question - https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map = {}
        l = 0
        maxf = 0

        for r in range(len(s)):
            if s[r] in map:
                map[s[r]] += 1
            else:
                map[s[r]] = 1
                
            maxf = max(maxf, map[s[r]])
            
            if (r-l+1) - maxf > k:
                map[s[l]] -= 1
                l += 1
                
        return (r-l+1)