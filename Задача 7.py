#Задача7
x = int(input())
a = x // 100 % 10
b = x // 10 % 10
c = x % 10
x = a + b + c
#1
if (int(x)>9) and (int(x)<100):
    print("является")
else:
    print('не является')
#2
x1 = a*b*c
if (int(x1)>99) and (int(x1)<1000):
    print("является")
else:
    print('не является')
#3
if (int(x1)>a):
    print("больше")
else:
    print('не больше')
#4
if (int(x)%5==0):
    print("кратна")
else:
    print('не кратна')
#5 
if (int(x)%a==0):
    print("кратна")
else:
    print('не кратна')