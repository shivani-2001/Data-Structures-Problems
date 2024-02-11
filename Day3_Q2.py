# Question - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Method 1 ->
        res = [1]*len(nums)

        pre = 1
        for i in range(1, len(nums)):
            pre = nums[i-1]*pre
            res[i] = pre
            
        post = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i]*post
            post = post*nums[i]

        return res