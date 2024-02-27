# Question - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        left, right = 0, len(height)-1

        while left<right:
            water = min(height[left], height[right])*(right-left)
            maxWater = max(water, maxWater)

            if height[left]<height[right]:
                left += 1
            else:
                right -= 1

        return maxWater