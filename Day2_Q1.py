class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Method 1 ->
        """for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]"""
                    

        # Method 2 ->
        seen = {}
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in seen:
                return [i, seen[diff]]
            else:
                seen[nums[i]] = i