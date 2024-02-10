# Question - https://leetcode.com/problems/group-anagrams/description/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Method 1 ->
        output = {}
        for s in strs:
            a = "".join(sorted(s))
            if a in output:
                output[a].append(s)
            else:
                output[a] = [s]

        return output.values()
