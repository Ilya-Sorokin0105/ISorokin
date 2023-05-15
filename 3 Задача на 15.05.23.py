def schet ():
    a = input ("Введите первое число: ")
    a = float (a)
    b = input ("Введите первое число: ")
    b = float (b)
    y = input ("Введите первое число: ")
    y = float (y)
    if a > b> y:
        print (a - b + y)
    else:
        print (b - a + y)
    return a, b, y  
c, d, r = schet ()