def obmen(): #zadacha 1
    c,a,b=[input('a:'),input('b:'),input('c:')]
    print(a,b,c)
obmen()

def check(): #zadanie 2.1
    a=(input('Введите первое число:'))
    b=(input('Введите второе число'))
    while True:
        try:
            a=float(a)
            b=float(b)
        except ValueError:
            print('Надо вводить числа')
            break

        else:
            print(a + b)
check()

def vvod(): #zadanie 2.2
    n = int(input('Введите количество чисел:'))
    a=[]
    for i in range(n):
        a.append(int(input(f'Введите переменную N{i+1}: ')))
    print(a)
vvod()

def diapazon():
    x=int(input('Введите любое число от 0 до 100:'))
    if (x>0) and (x<100):
        print(x*5)
    else:
        print('Вы ввели число не из диапазона')
diapazon()