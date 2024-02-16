# Question - https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        temp = []

        def valid_comb(left, right):
            if left == right == n:
                output.append("".join(temp))
                return

            if left < n:
                temp.append("(")
                valid_comb(left+1, right)
                temp.pop()

            if right < left:
                temp.append(")")
                valid_comb(left, right+1)
                temp.pop()

        valid_comb(0, 0)
        return output