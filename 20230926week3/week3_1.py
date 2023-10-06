#1 十进制到二进制小数转换
import math
def dec_to_bin_integer(target):
    if target == 0:
        return "0"
    d_int = math.floor(target)

    binary = ""
    while d_int > 0:
        binary = str(d_int % 2) + binary
        d_int //= 2
    return binary
def dec_to_bin_float(target):
    binary = ""
    d_float = target - math.floor(target)

    while d_float != 0:
        d_float *= 2
        if d_float >= 1:
            binary += "1"
            d_float -= 1
        else:
            binary += "0"
    return binary

a = eval(input())
str1 = dec_to_bin_integer(a)
str2 = dec_to_bin_float(a)
print(str1 + "." + str2)