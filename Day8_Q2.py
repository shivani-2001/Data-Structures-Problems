# Question - https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i in range(len(heights)):
            index1 = i

            while stack and (heights[i] < stack[-1][1]):
                index, value = stack.pop()
                area = (i-index)*value
                maxArea = max(area, maxArea)
                index1 = index
                
            stack.append((index1, heights[i]))
        
        n = len(heights)
        while stack:
            index, value = stack.pop()
            area = (n-index)*value
            maxArea = max(area, maxArea)
                
        return maxArea