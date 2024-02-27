# Question - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right

        while left<=right:
            mid = (left+right)//2
            total_hours = 0

            for p in piles:
                total_hours += -(-p//mid)

            if total_hours>h:
                left = mid+1
            else:
                res = mid
                right = mid-1
                
        return res