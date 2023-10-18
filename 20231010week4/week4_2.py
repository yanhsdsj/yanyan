#2
import time
start = time.perf_counter()
def fun(a):
    flag = 0
    if a > 2:
        for i in range(2, a):
            if a % i == 0:
                flag = 1

    if flag == 0:
        print("yes")
    else:
        print("no")

end = time.perf_counter()

a = int(input())


time = end - start

print(format(time))
