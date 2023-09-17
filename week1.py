#1 3
print("Hello World")

print("闫研10225501446")
#4
print(chr(0x2605)*10)
print(chr(0x2605)+"数据科学工程导论"+chr(0x2605))
print(chr(0x2605)*10)
#5
x = int(input())
y = int(input())
z = int(input())

if x > y:
    s = y
    y = x
    x = s

if x > z:
    s = z
    z = x
    x = s

if y > z:
    s = z
    z = y
    y = s

print(x,y,z)
#6
ls = []
w = int(input())
x = int(input())
y = int(input())
z = int(input())

ls.append(w)
ls.append(x)
ls.append(y)
ls.append(z)

ls.sort()
print(ls)
#7
for i in range(1,101):
    if i % 2 == 1:
        print(i)
#8
s = 0
for i in range(1,101):
    s += i
print(s)
#9
cnt = int(input())
numbers = []
for i in range(0,cnt):
    number = int(input())
    numbers.append(number)

numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
#10
S = input()
l = len(S)
cnt = 1
ch = ""
for i in range(1,l):
    if S[i] == S[i-1]:
        cnt += 1

if cnt != 1:
    print("yes")
else:
    print("no")

#11
S = input()
l = len(S)
newlist = []
for i in range(0,l):
    if S[i] != " ":
        newlist.append(S[i])
print("".join(newlist))

#12
import math
n = float(input())
number = abs(n)
if number >= 1:
    low = 1.0
    up = number
    a = 0.0001
else:
    low = number
    up = 1.0
    a = 0.0001
m = 3
while True:
    mid = (low+up)/2
    if abs(math.pow(mid,m) - number) < a :
        if n > 0:
            print(mid)
        else:
            print(0-mid)
        break
    else:
        if math.pow(mid,m) > number:
            up = mid
        if math.pow(mid,m) < number:
            low = mid


#13
n = int(input())
res = 1
for i in range(1,n+1):
    res *= i
print(res)