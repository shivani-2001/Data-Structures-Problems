nums = [1,3,-1,-3,8,5,3,6,7]
k = 3
print(nums[-0-1:-0-1-k:-1])

maxwindow = []
for i in range(0, (len(nums)-k+1)//2):
    print(i)
    maxwindow.append(max(nums[i:k+i]))
    maxwindow.append(max(nums[-(i+1):-(k+i+1):-1]))

print(maxwindow)