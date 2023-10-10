#8 随机生成多组长度递增的随机数列
#  用不同的排序算法进行排序
#  比较不同算法在不同长度数列下的运行效果
import math
import random
import time

n = random.randint(1,10000)
print(n)
arr1 = []
arr2 = []
for i in range(0, n):
    arr1.append(random.randint(0,1000000))
    arr2.append(arr1[i])
print(arr1)

#选择排序
def selection_sort(arr):
    for i in range(0,n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        #交换两个数的值
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


#归并排序
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


start1 = time.perf_counter()
selection_sort(arr1)
end1 = time.perf_counter()
ts1 = end1 - start1
print(format(ts1))
print(selection_sort(arr1))

start2 = time.perf_counter()
merge_sort(arr2)
end2 = time.perf_counter()
ts2 = end2 - start2
print(format(ts2))
print(merge_sort(arr2))

