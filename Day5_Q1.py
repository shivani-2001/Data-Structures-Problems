# Question - https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        if len(nums) == 0:
            return 0

        max1 = 1
        i = 1

        for n in range(len(nums)-1):
            if nums[n]+1 == nums[n+1]:
                i+=1
            elif nums[n] == nums[n+1]:
                continue
            else:
                if max1 < i:
                    max1 = i
                i = 1
                
        if max1 < i:
            max1 = i

        return max1