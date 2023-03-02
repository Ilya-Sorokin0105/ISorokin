#Задача 3
x = int(input())
a = x // 100 % 10
b = x // 10 % 10
c = x % 10
x1 = c * 100 + b*10 + a
print (x-x1)