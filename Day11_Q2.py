# Question - https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        mid = (left+right)//2

        while left<=right:
            if target<nums[mid]:
                right = mid-1
            elif target>nums[mid]:
                left = mid+1
            else:
                return mid
            
            mid = (left+right)//2

        return -1
