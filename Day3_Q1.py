# Question - https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Method 1 ->
        counts = {}
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1

        counts = sorted(counts.items(), key=lambda x:x[1], reverse=True)
        return [i for i, j in counts[:k]]