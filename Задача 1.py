n = (input())
if (int(n)>999) and (int(n)<10000):
    a = int(n[0])+int(n[1])+int(n[2])+int(n[3])
    b = int(n[0])*int(n[1])*int(n[2])*int(n[3])
    print (a)
    print (b)
else:
    print("не четырехзначное число")