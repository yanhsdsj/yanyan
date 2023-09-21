#9 蒙特卡洛定积分
import random
import math
sum = 0
for i in range(1, 1000000):
    x = random.uniform(2, 3)
    y = random.uniform(0, 30)
    if y <=  x ** 2 + 4 * x * math.sin(x):
        sum = sum + 1
print(x,y)
print(sum)
print(sum/1000000*30)