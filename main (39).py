#1
def не_обязан(a):
    a = str(a)
    if len(a) != 4: 
        print("Не 4х значное число")
    else:
        sum = int(a[0]) + int(a[1]) + int(a[2]) + int(a[3])
        proizv = int(a[0]) * int(a[1]) * int(a[2]) * int(a[3])
    return(sum, proizv)
print(не_обязан(int(input("введите 4х значное число: "))))
#2
def gg(a):
    a = str(a)
    if len(a) != 5: 
        print("Не 5 значеное число")
    else: return a[3], a[4]
print(gg(int(input("Введите 5 значное число: "))))
#3
def обязан(a):
    a = str(a)
    if len(a) != 3: print("Не 3 значное число")
    else: 
        b = a[2] + a[1] + a[0]
    return int(a) - int(b)
print(обязан(int(input("Введите 3х значное число: "))))
#4
def print_digits(n):
    digits = []
    while n > 0:
        digit = n % 10
        digits.append(digit)
        n //= 10
    digits.reverse()
    print(digits)
#5    
def dvass(a):
    a = str(a)
    l = len(a)
    flag = False
    for i in range(l):
        if int(a[i]) == 2:
            flag = True
    return flag
print(dvass(int(input("Введите число: "))))

