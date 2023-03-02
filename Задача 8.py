x = int(input())
a = x // 1000 % 10
b = x // 100 % 10
c = x // 10 % 10
d = x % 10
x1 = a+b+c+d
x2 = a*b*c*d
#1
if int(a+b) == int(c+d):
    print("Равняется")
else:
    print('не равняется')
#2
if (int(x1)%3==0):
    print("кратна")
else:
    print('не кратна')
#3
if (int(x2)%4==0):
    print("кратна")
else:
    print('не кратна')
#4
if (int(x2)%a==0):
    print("кратна")
else:
    print('не кратна')
