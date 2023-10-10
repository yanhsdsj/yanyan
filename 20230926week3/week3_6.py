#6 if语句实现百分之转等级制
score = int(input())
if score < 60:
    print("不合格")
elif 60 <= score <= 74:
    print("合格")
elif 75 <= score <= 89:
    print("良好")
else:
    print("优秀")