totalSum = 0

global totalSum

for i in range(1, 1000):
        if (i % 3 == 0 or i % 5 == 0):
            totalSum += i

print(totalSum)