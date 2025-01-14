import math
acc = 0
mean = 6.99
nums = [3.1, 3.3, 4.2, 6.0, 6.2, 6.8, 7.1, 7.1, 7.1, 7.2, 7.4, 8.0, 8.7, 9.2, 10.0, 10.5]
for num in nums:
  acc += (num - mean)**2

result = acc/(len(nums)-1)

print(math.sqrt(result))

acc = 0
for num in nums:
  acc += num

print(acc/len(nums))