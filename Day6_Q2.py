# Question - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for i in tokens:
            if i in ["+", "-", "*", "/"]:
                num2 = nums.pop()
                num1 = nums.pop()
                if i == "+":
                    nums.append(num1+num2)
                elif i == "-":
                    nums.append(num1-num2)
                elif i == "*":
                    nums.append(num1*num2)
                else:
                    nums.append(int(num1/num2))

            else:
                nums.append(int(i))
        return nums[-1]