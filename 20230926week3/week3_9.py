#构建数组

import math
n = int(input())
A = []
B = []
for i in range(0, n):
    A.append(int(input()))

for j in range(0, n):
    B.append(1)

    for k in range(0, n):
        if (j != k):
            B[j] *= A[k]

    print(B[j])