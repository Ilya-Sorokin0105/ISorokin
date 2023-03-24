a = int(input())
if a%4 ==0:
    if a%100 ==0:
        print('Столетие')
        if a%400 ==0:
            print("високосный")
        else:
            print("обычнй")
    else:
        print('год високосный')
else:
    print("обычный")
