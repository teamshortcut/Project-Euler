primeNumbers = [1, 2]
append = False

for i in range (3, 10000000, 2):
    for j in primeNumbers:
        if (i % j != 0):
            append = False
        elif (i % primeNumbers[j]):
            append = True
        else:
            append = False
    if (append == True):
        primeNumbers.append(i)
        print(primeNumbers)

print(primeNumbers)