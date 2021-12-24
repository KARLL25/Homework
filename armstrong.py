def colch(n):
    n=str(n)
    return len(n)
def namin(n):
    n=str(n)
    mas=[]
    for l in n:
        mas+=[l]
        mas.sort()
    return mas
masISKL=[]
for i in range(1,10**40):
    razriad= colch(i)
    ver=namin(i)
    otv=0
    if ver!=masISKL:
        for j in range(razriad):
            otv+=int(ver[j])**razriad
        if i==otv:
            print(i)
            masISKL+=ver
print(masISKL)
