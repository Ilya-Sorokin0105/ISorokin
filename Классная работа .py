#1
import random
a = random.randint(1, 20)
b = random.randint(1, 20)
print(a, b)
g = int(input())
if g == a+b:
    print("Верно")
else:
    print("Не верно, правильный ответ:", a+b)
#2
a = int(input())
b = int(input())
if 99 < a < 1000:
    x1 = a // 100 % 10
    x2 = a // 10 % 10
    x3 = a % 10
    g = x1 + x2 + x3
    if g > b:
        print("Сброс")
        a = 0
    else:
        print("Сегодня не сломался")
        print(a)
else:
    pass
#3
a = int(input("Количество отработанных часов: "))
b = int(input("Остаток по кредиту: "))
c = int(input("Деньги на еду: "))
d = b + c
dd = ((200 * a) / 2**3) + a
if dd >= d:
    print("Часов хватает. Можно отдохнуть")
else:
    print("Часов не хватает. Придётся работать")