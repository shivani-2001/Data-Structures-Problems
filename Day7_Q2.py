# Question - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        temp = []

        for i in range(len(temperatures)):
            while temp and temperatures[i]>temp[-1][0]:
                value, index = temp.pop()
                res[index] = i - index

            temp.append([temperatures[i], i])

        return res