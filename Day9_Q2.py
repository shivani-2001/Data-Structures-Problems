class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Method 1 ->
        for i in range(len(numbers)-1):
            for j in range(1, len(numbers)):
                if numbers[i]+numbers[j] > target:
                    break
                if numbers[i]+numbers[j] == target:
                    return [i+1, j+1]
                
        # Method 2 ->
        a, b = 0, len(numbers)-1

        while a<b:
            if numbers[a]+numbers[b]<target:
                a+=1
            elif numbers[a]+numbers[b]>target:
                b-=1
            else:
                return [a+1, b+1]