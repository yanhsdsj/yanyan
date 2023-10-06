#1 判断输入数是否为质数
a = int(input())
flag = 0
if a > 2:
    for i in range(2, a):
        if a % i == 0:
            flag = 1

if flag == 0:
    print("yes")
else:
    print("no")
