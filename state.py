from copy import deepcopy
import math


class State:
    # 深度最大值
    max_deep = 10
    # 目标状态
    end = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

    """
    output:无
    """
    def __init__(self, state, deep, parent=None):  # 初始化函数
        self.state = state  # 节点状态
        self.deep = deep    # 深度
        self.parent = parent    # 父节点
        self.cost = None

    """
     output：错位代价
    """
    def position_cost(self, state):  # 计算曼哈顿距离之和,state为目标状态
        count = 0  # 计数器
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 1:
                    count += i+j
                if self.state[i][j] == 2:
                    count += abs(i+j-1)
                if self.state[i][j] == 3:
                    count += abs(i+j-2)
                if self.state[i][j] == 4:
                    count += abs(i+j-3)
                if self.state[i][j] == 5:
                    count += abs(i+j-4)
                if self.state[i][j] == 6:
                    count += abs(i+j-3)
                if self.state[i][j] == 7:
                    count += abs(i+j-2)
                if self.state[i][j] == 8:
                    count += abs(i+j-1)
        return count

    def calculate_cost(self):
        end_state = State.end  # 目标状态
        h_cost = self.position_cost(end_state)
        # 此处为A*算法，启发函数f(n) = d(n) + w(n),即f(n) = 搜索树的深度 + 曼哈顿距离
        self.cost = self.deep + h_cost

    """ 
    output：节点代价  
    """
    def get_cost(self):  # 获取节点f(n)（代价函数）
        self.calculate_cost()  # 计算cost
        return self.cost

    """ 
    output：空白(0)的坐标 
    """
    def find_zero_pos(self):  # 寻找当前节点状态中空白的坐标
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    """
    output：后继子节点集sub_States  
    """
    def get_subs(self):  # 获取当前节点的扩展出的后继子节点
        sub_states = []  # 子节点集合
        x, y = self.find_zero_pos()  # 获取空白（0）的坐标位置
        if self.deep >= self.max_deep:  # 如果深度大于规定最大深度，返回空，目的为避免深度一直拓展
            return sub_states

        # 上移
        # 深拷贝一份self.state到s
        # 移动（修改s的内容不会影响原本的self.state）
        # 初始化新节点new （利用State类的构造函数，参数列表为(state, deep, parent)）
        # new加入到sub_states
        if x > 0:
            s = deepcopy(self.state)
            s[x][y], s[x-1][y] = s[x-1][y], s[x][y]
            new = State(s, self.deep + 1, self)
            sub_states.append(new)
        # 下移
        if x < 2:
            s = deepcopy(self.state)
            s[x][y], s[x + 1][y] = s[x + 1][y], s[x][y]
            new = State(s, self.deep + 1, self)
            sub_states.append(new)
        # 左移
        if y > 0:
            s = deepcopy(self.state)
            s[x][y - 1], s[x][y] = s[x][y], s[x][y - 1]
            new = State(s, self.deep + 1, self)
            sub_states.append(new)
        # 右移
        if y < 2:
            s = deepcopy(self.state)
            s[x][y + 1], s[x][y] = s[x][y], s[x][y + 1]
            new = State(s, self.deep + 1, self)
            sub_states.append(new)

        return sub_states

    """ 
    print函数：打印当前节点状态
    无input，output 
    """
    def print(self):
        for i in range(3):
            for j in range(3):
                print(self.state[i][j], end='   ')
            print("\n")