#1 正整数列表乘积最大
n = int(input())
if n <= 3:
    if n == 1:
        result = 0
    if n == 2:
        result = 1
    if n == 3:
        result = 2
else:
    if n % 3 == 0:
        result = 3 ** (n/3)
    elif n % 3 == 1:
        result = 3 ** (n//3 - 1) * 2 * 2
    else:
        result = 3 ** (n//3) * 2

print(result)
#分解成以3为“底”的乘积 余1时拆一个3作2*2 余2时在原来的基础上再*2