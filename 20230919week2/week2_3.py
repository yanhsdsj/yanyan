#3 渡河问题

def is_valid_state(state):
    # 检查是否有不安全的状态，即狼吃羊或羊吃菜
    if (state[1] == state[2] and state[0] != state[1]) or (state[2] == state[3] and state[0] != state[2]):
    #0-人 1-狼 2-羊 3-菜
        return False
    return True

def dfs(state, path, visited):
    if state == (0, 0, 0, 0):
        # 找到了解决方案
        print("找到解决方案：", path)
        return

    for move in moves:
    #寻找能加入集合的渡河步骤
        new_state = tuple(state[i] + move[i] for i in range(4))#tuple为元组 是有序且不可更改的集合
        if all(0 <= new_state[i] <= 1 for i in range(-1, 3)) and is_valid_state(new_state) and new_state not in visited:
            visited.add(new_state)
            dfs(new_state, path + [new_state], visited)
            visited.remove(new_state)


# 初始状态：(1, 1, 1, 1) 表示人、狼、羊、菜都在起始岸
initial_state = (1, 1, 1, 1)
# 移动方式
moves = [
    (-1, 0, 0, 0),
    (-1, -1, 0, 0),
    (-1, 0, -1, 0),
    (-1, 0, 0, -1),
    (1, 0, 0, 0),
    (1, 1, 0, 0),
    (1, 0, 1, 0),
    (1, 0, 0, 1)
]
#一共有4*2种安全移动的方法

visited = set()
#visited = []
#创建不允许有重复的集合
visited.add(initial_state)
#增加一个元素值
dfs(initial_state, [initial_state], visited)