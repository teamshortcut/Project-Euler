import math

"""
#Method to work out all factors of a number. On large numbers can take a very long time to run.
number = 13195

factors = []

for i in range (1, number + 1):
    if (number % i == 0):
            factors.append(i)
            print(i)

print(factors)
#At this point to work out hight prime factor, you can look at the console results and manually check each number (starting from highest) to see if it is prime.
#It's a bit of a cheaty solution, but it works. :/
"""
#Method to work out all prime factors. Still a pretty rubbish solution.
number = 600851475143
newNumber = 600851475143

for i in range (1, math.ceil(math.sqrt(number))):
    if (newNumber % i == 0):
        newNumber = number / i
        number = newNumber
        print(number)
        print(newNumber)

print(newNumber)