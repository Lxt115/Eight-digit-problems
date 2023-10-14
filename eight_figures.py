from state import State

""" 
input：
    state:状态
output:
    state的cost
"""


def get_cost(state):
    return state.get_cost()


"""    
solve函数：8数码寻路函数，利用不同方式找到初始8数码状态到最终8数码状态的路径
input: 
    start_state:初始状态,类型：np.array，3*3
    end_state:最终状态,类型：np.array，3*3
    错位启发
output：
    [a,b] = [close_list,len(close_list)-1]形式
    a（close_list）：最终路径节点集合
    b:步数
"""


def solve(start_state, end_state):
    closed_list = []  # 闭集
    open_list = []  # 开集
    ini = State(start_state, 0, None)  # 初始化节点
    open_list.append(ini)

    while True:
        # 如果开集一开始为空，则失败，退出
        if len(open_list) == 0:
            print("FAIL")
            break
        # 开集根据节点的cost（f()）来升序排列
        ordered_list = sorted(open_list, key=get_cost)
        # 拿出第一个结点，即f(x)最小的结点n
        min_n = ordered_list[0]
        # 将n放入闭集
        closed_list.append(min_n)
        # 将n移出开集
        open_list.remove(min_n)
        # 如果n达到目标状态，打印结果，结束
        if min_n.state == end_state:
            print_closed(closed_list)
            break
        # 获取n的后继子结点集
        son_states = min_n.get_subs()
        # 判断n的后继子结点集是否在在开集与闭集中出现
        for a in son_states:
            flag = 0
            for b in open_list:
                if a.state == b.state:
                    flag = 1
            for c in closed_list:
                if a.state == c.state:
                    flag = 1
            if flag == 0:
                open_list.append(a)  # 未出现，则讲该子节点加入开集
    # 返回闭集与路径步数
    return [closed_list, len(closed_list) - 1]


"""  
print_inf函数：打印从初始状态到达目标转态的路径
input：
    res：结果集，类型为[State,...]
无output
"""


def print_closed(closed_list):
    print("########################")
    for i, each in enumerate(closed_list):
        if i == 0:
            print("第%d步：" % i)
        else:
            print("=>第%d步：" % i)
        each.print()
    print("总共%d步" % (len(closed_list) - 1))
    print("########################")


def print_path(state):
    if state is None:
        return
    else:
        print_path(state.parent)
        print('-'*10)
        state.print()
        print('-' * 10)
        print('    ↓    \n')


if __name__ == "__main__":

    start = [[2, 8, 3], [1, 6, 4], [7, 0, 5]]
    end = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

    res = solve(start, end)
    print("共计%d步\n" % (res[1]))
