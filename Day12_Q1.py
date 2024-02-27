# Question - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Method 1 ->
        for i in matrix:
            if target in i:
                return True

        return False

        # Method 2 ->
        for nums in matrix:
            if nums[-1]>=target:
                left, right = 0, len(nums)-1
                mid = (left+right)//2

                while left<=right:
                    if target<nums[mid]:
                        right = mid-1
                    elif target>nums[mid]:
                        left = mid+1
                    else:
                        return True
                    
                    mid = (left+right)//2

        return False