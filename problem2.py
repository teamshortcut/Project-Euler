firstTerm = 1
secondTerm = 2
thirdTerm = 0

totalSum = firstTerm + secondTerm
evenSum = secondTerm

for i in range (1, 4000000):
    if (secondTerm <= 4000000):
        thirdTerm = firstTerm + secondTerm
        firstTerm = secondTerm
        secondTerm = thirdTerm
        #totalSum += secondTerm
        #print(firstTerm)
        #print(secondTerm)
        if (secondTerm % 2 == 0):
            evenSum += secondTerm
            print(evenSum)
    else:
        print(i)
        break

print(evenSum)