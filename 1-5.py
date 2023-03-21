#1 
a = int(input()) 
if (int(a)>9) and (int(a)<100):
    b = a // 10 % 10 
    c = a % 10 
    print(c*10+b) 
else: 
    print("Число не двухзначное")

#2
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())

a = (x2 - x1)**2 + (y2 - y1)**2
b = (x3 - x2)**2 + (y3 - y2)**2
c = (x1 - x3)**2 + (y1 - y3)**2

a = a ** 0.5
b = b ** 0.5
c = c ** 0.5
print(a, b ,c)


P = a + b + c
print(P)

#3
a = int(input()) 
if (int(a)>9) and (int(a)<100):
    b = a // 10 % 10 
    c = a % 10 
    print(b, "десятки") 
    print(c, "единицы")
else: 
    print("Число не двухзначное")
    
#4
cm = int(input("Введите см: "))
dc = int(input("Введите дц: "))
mm = int(input("Введите мм: "))
m = cm * 100
m1 = dc / 10
m2 = mm * 1000
print("см =", m,'m', "дц =", m1,'m', "мм =", m, 'm' )

#5
k = int(input("Введите k: "))
x = int(input("Введите x: "))
if k < x:
    y = k*x
elif k > x:
    y = k+x
else:
    y = k/x
print(y)