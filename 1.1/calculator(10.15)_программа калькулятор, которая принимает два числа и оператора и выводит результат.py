def Calc(a,b,c):
    result=0
    try:
        a = float(a)
        b = str(b)
        c = float(c)
    except ValueError:
        print('Либо ввели не число, либо пустое значение')
    else: 
        if b=='+':
            result=a+c
            return result
        elif b=='-':
            result=a-c
            return result
        elif b=='/':
            try:
                result=a/c
            except ZeroDivisionError:
                print("На ноль делить нельзя!")
                return "Error"
            return result
        elif b=='*':
            result=a*c
            return result
        elif b =="^" or b=="**":
            result=a**c
            return result
        else:
            print("Неизвестный оператор")
while True:
    a = input('Введите число ')
    b = input('Введите функцию ')
    c = input('Снова число ')
    print(Calc(a,b,c))
