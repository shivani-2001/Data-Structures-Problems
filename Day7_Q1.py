# Question - https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def backtrack(s, left, right):
            if len(s) == 2 * n:
                output.append(s)
                return

            if left < n:
                backtrack(s + '(', left + 1, right)

            if right < left:
                backtrack(s + ')', left, right + 1)

        backtrack("", 0, 0)
        return output