def sort(massiv):
    p = 0
    i = 0
    j = 0
    while (i < len(massiv)):
        p = massiv[i]
        j = i - 1
        while (j >= 0 and p < massiv[j]):
            massiv[j + 1] = massiv[j]
            j -= 1

        massiv[j + 1] = p
        i += 1
    return massiv


def sortt(masiv):
    p = 0
    i = 0
    j = 0
    while (i < len(masiv)):
        p = masiv[i]
        j = i - 1
        while (j >= 0 and perviy(p,masiv[j])):
            masiv[j + 1] = masiv[j]
            j -= 1
        masiv[j + 1] = p
        i += 1
    return masiv

def perviy(arr1,arr2):
    for i in range(len(arr1)):
        if arr1[i]==arr2[i]:
            continue
        return arr1[i]<arr2[i]


def read_file(filename_read=""):
    with open(filename_read, 'r') as file:
        masiv = []
        for s in file:
            mas=[]
            c=s.split('\n')[0]
            c=c.split( )
            massiv=[]
            for k in c:
                k=int(k)
                massiv.append(k)
            sort(massiv)
            masiv.append(massiv)
    return masiv

masiv=[]
massiv2=[]
mas=[]
filename_read = input("Напишите имя файла с массивом: ")
masiv=read_file(filename_read)
masiv=sortt(masiv)
print(masiv)
for i in range(len(masiv)):
     for j in range(len(masiv[i])):
         print(masiv[i][j], end=' ')
     print()
