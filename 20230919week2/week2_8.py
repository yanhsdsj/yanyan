#8 求pi
import math
import random
import time


start1 = time.perf_counter()
def Pi():
    sum = 0
    for i in range(1, 10000000):
        x = random.random()
        y = random.random()
        d = x * x + y * y
        if d <= 1:
            sum += 1
    return (sum/10000000 * 4)
end1 = time.perf_counter()



start2 = time.perf_counter()
val = math.pi
end2 = time.perf_counter()



start3 = time.perf_counter()
PI = math.atan(1)*4
end3 = time.perf_counter()



x = Pi()
print(x)
print(val)
print(PI)



ts1 = end1 - start1
print(format(ts1))
ts2 = end2 - start2
print(format(ts2))
ts3 = end3 - start3
print(format(ts3))


