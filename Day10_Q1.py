# Question - https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            j, k = i+1, len(nums)-1
            while j<k:
                if nums[i]+nums[j]+nums[k]<0:
                    j += 1
                elif nums[i]+nums[j]+nums[k]>0:
                    k -= 1
                else:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j<k:
                        j += 1

        return triplets