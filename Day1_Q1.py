# Question - https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Method 1 ->
        """res = False
        count = []
        for i in nums:
            if i in count:
                res = True
                return res
            else:
                count.append(i)
        
        return res"""
        
    
        # Method 2 ->
        """res = {}
        for a in nums:
            if a in res:
                res[a]+=1
            else:
                res[a] = 1
                
        res = res.values()
        if any(v for v in res if v>1):
            return True
        else:
            return False"""
            
            
        # Method 3 ->
        nums1 = set(nums)
        if len(nums1) == len(nums):
            return False
        else:
            return True