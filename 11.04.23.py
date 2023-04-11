#6
i = 2
while i in range(2, 42):
    print (i)
    i+=2   

#7
a = 0
b = 1
n = 30
i = 0
while i < n:
    i = i + b
    if i // 2:
        i = i + 1 
        print(i)

#8
b = 2
n = 20
i = 0
while i < n:
    i = i + b
    c = i ** 0.5
    print("корень из", i, c)
    
#9
a = int(input("Введите сколько стоит 1кг"))
b = 1
n = 10
i = 0
while i < n:
    i = i + b
    i1 = i * a
    print("Кг:",i)
    print("Cтоимость:", i1)
    
#10
a = int(input("Точка начала отрезка"))
b = int(input("Точка конца отрезка"))
while a<=b:
    print(a**0.5)
    a += 1
    
#11
a = int(input())
b = int(input())
while a < b: 
    y = a ** 2 - 1
    print(y)
    a += 1
    
#12
a = int(input())
b = int(input())
while a < b: 
    y = 1/2*a
    print(y)
    a += 1
    
#13
a = int(input())
b = int(input())
while a < b: 
    y = (a - 1)**2
    print(y)
    a += 1
    
#14
x = 0
while x <= 20: 
    t = 1 + x
    y = (2 * t**2) + 2 * t + 2
    print(y)
    x += 1
    
#15
x = 2
while x <= 20: 
    f = 2 * x
    y = 8 * (f**2) - f
    print(y)
    x += 1
    
    
    
    
    