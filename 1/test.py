import math

list1 = [3.1, 3.3, 4.2, 6.0, 6.2, 6.8, 7.1, 7.1, 7.1, 7.2, 7.4, 8.0, 8.7, 9.2, 10.0, 10.5]
acc = 0
for i in list1:
  acc += i

print(acc/len(list1))

mean = 6.99
new = [round((ball-mean)**2, 2) for ball in list1]
print(new)

acc2 = 0
for n in new:
  acc2 += n

standard_dev = round(math.sqrt(acc2/(len(new)-1)), 2)
print(standard_dev**2)