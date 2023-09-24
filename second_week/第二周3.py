#(H->Human,W->Wolf,S->Sheep,V->Vegetable)
name = ["H", "W", "S", "V"]
search_finish = False; # 用于判定 递归截止

# 完成状态的判断
def is_done(status):
    return status[0] and status[1] and status[2] and status[3]

# 生成下一个局面的所有情况
def generate_next_status(status):
    next_status_list = []

    for i in range(0, 4):
        if status[0] != status[i]: # 和农夫不在一侧？
            continue

        next_status = [status[0],status[1],status[2],status[3]]
        # 农夫和其中一个过河，i 为 0 时候，农夫自己过河。
        next_status[0] = not next_status[0] # 农夫自身取反
        next_status[i] = next_status[0] # 和农夫一起过河
        # 如果是安全的状态, 那么将本次状态加入状态列表
        if is_valid_status(next_status):
            next_status_list.append(next_status)

    return next_status_list

# 判断是否合法的局面 安全局面
def is_valid_status(status):
    if status[1] == status[2]:
        if status[0] != status[1]:
            # 狼和羊同侧，没有人在场 不安全
            return False

    if status[2] == status[3]:
        if status[0] != status[2]:
            # 羊和草同侧，没有人在场 不安全
            return False
    return True

# 搜索程序
def do_search(history_status):
    global search_finish

    if search_finish:
        return

    current_status = history_status[len(history_status) - 1] # 获取当前状态

    next_status_list = generate_next_status(current_status) # 生成下一次状态
    for next_status in next_status_list:
        # 去重处理
        if next_status in history_status:
            continue
            
        history_status.append(next_status) # 加入下一个状态
        # 完成后输出
        if is_done(next_status):
            search_finish = True
            print(get_solution(history_status))
        else:
            do_search(history_status) # 未完成则继续搜索

        history_status.pop()

#根据前后状态输出过河指标 过去的状态和现在的状态对比
def output_cross(pre, now):
    res = [] # 用于存放当前数据
    for i in range(len(pre)):
        if pre[i] != now[i]:
            res.append(name[i])
    return ''.join(res)

#打印过程 根据历史栈 转换成 过河标识
def get_solution(history_status):
    result = ''
    hs_len = len(history_status)
    for i in range(hs_len):
        # output_cross
        # 从第二个开始 比较
        if i > 0:
            result += output_cross(history_status[i-1], history_status[i])
            # 不是最后一个
            if i != hs_len - 1:
                result += ' '
    return result

if __name__ == "__main__":
    # 初始化第一次状态
    status = [False, False, False, False]
    # 初始化历史状态
    history_status = [status]
    # 触发搜索
    do_search(history_status)
