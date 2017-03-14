palidromes = []

def palindromeCheck(var):
    if (str(var) == str(var)[::-1]):
        print(str(var))
        return True
    else:
        print("Nope")
        return False

for i in range (1, 1000):
    for j in range (1, 1000):
        if (palindromeCheck(i * j) == True):
            palidromes.append(i * j)

print(palidromes)
print(max(palidromes))