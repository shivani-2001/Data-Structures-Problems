# Question - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = float('inf')
        left = 0
        right = len(nums)-1

        while left<=right:
            mid = (left+right)//2
            if nums[mid]>=nums[left]:
                low = min(low, nums[left])
                left = mid+1
            else:
                low =  min(low, nums[mid])
                right = mid-1

        return low