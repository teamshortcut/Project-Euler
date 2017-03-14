number = 2432902008176640000

#Find smallest possible multiple of 1-20.
listx = []

for i in range (2520, number, 2520):
    print(i)
    if (i % 20 == 0):
        if(i % 19 == 0):
            if (i % 18 == 0):
                if (i % 17 == 0):
                    if (i % 16 == 0):
                        if (i % 15 == 0):
                            if (i % 14 == 0):
                                if (i % 13 == 0):
                                    if (i % 12 == 0):
                                        if (i % 11 == 0):
                                            listx.append(i)
                                            break

print(listx)
"""
#Find smallest multiple of 1-10.
listx = []

for i in range (1, 3000):
    print(i)
    if ((i % 1 == 0) and (i % 2 == 0) and (i % 3 == 0) and (i % 4 == 0) and (i % 5 == 0) and (i % 6 == 0) and (i % 7 == 0) and (i % 8 == 0) and (i % 9 == 0) and (i % 10 == 0)):
        #print(i)
        listx.append(i)
        break
30040200
print(listx)"""