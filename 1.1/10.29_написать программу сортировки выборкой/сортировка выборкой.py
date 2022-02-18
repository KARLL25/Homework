def file():
    import random
    file=open("s.txt","w")
    a=[x for x in range(300)]
    random.shuffle(a)
    for l in a:
        file.write(str(l))
        file.write("\n")

def sortirovka_viborka(nums):  
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
print("Маркелов Даниил 14122 Программа сортирует созданный файл при помощи метода: Сортировка выборкой")
 
while True:
        offer=input("Создать файл sortirovka.txt с случайными числами от 0 до 300? [Да\Нет] ")
        if offer=="Да":
            file()
            break
        elif offer=="Нет":
            print
            break
        print("\n")
with open('s.txt') as n:
    text=[int(x) for x in n]
sortirovka_viborka(text)  
print(text)
