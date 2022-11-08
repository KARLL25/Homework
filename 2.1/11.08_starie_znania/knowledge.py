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

def diapazon(): #zadanie 3.1
    x=int(input('Введите любое число от 0 до 100:'))
    if (x>0) and (x<100):
        print(x*5)
    else:
        print('Вы ввели число не из диапазона')
diapazon()

def fibanacchi(): #zadanie 4
    x1, x2 = 1, 1
    print ('Введите число в пределах от 0 до 250: ')
    n = int ( input() )
    while 999 < n or n < 1:
        print('Неверное число')
        print ('Введите число в пределах от 0 до 250: ')
        n = int( input())
    while x2 < n:
      F = x1 + x2
      x1=x2
      x2=F
    res = ''
    if n != x2:
        res = 'не '
    print ( 'Число', n, res, 'является числом Фибоначи')
fibanacchi()
