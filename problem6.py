sumVar = 0
squares = 0

for i in range (1, 101):
    sumVar += i

for i in range (1, 101):
    squares += i**2

print(sumVar**2)
print(squares)
print(sumVar**2 - squares)