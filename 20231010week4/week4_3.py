#3 插入排序
import random
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = []
n = random.randint(1000,3000)
for i in range(1, n):
    x = random.randint(1, 10000)
    arr.append(x)

print(insertion_sort(arr))
print(arr)
