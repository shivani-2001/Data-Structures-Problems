# Question - https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.data.get(key, [])

        left, right = 0, len(values)-1
        while left <= right:
            mid = (left+right)//2
            if values[mid][1] == timestamp:
                return values[mid][0]
            
            elif values[mid][1] < timestamp:
                if values[mid][1] == values[-1][1] or values[mid+1][1] > timestamp:
                    return values[mid][0]
                else:
                    left = mid+1
            else:
                right = mid-1

        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)