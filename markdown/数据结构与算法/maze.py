# -- coding: utf-8 --
# 迷宫问题
import time

matrix = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1]
]

dirs = [
    lambda x, y: (x + 1, y),  # 右
    lambda x, y: (x - 1, y),  # 左
    lambda x, y: (x, y - 1),  # 下
    lambda x, y: (x, y + 1),  # 上
]


# 栈 - 深度优先
def maze_path(x1, y1, x2, y2):
    """

    :param x1:  起点
    :param y1:
    :param x2:  终点
    :param y2:
    :return:
    """
    stack = []
    stack.append((x1, y1))
    while stack:
        cur_node = stack[-1]  # 当前节点的位置
        if cur_node[0] == x2 and cur_node[1] == y2:
            # 走到终点：
            for i in stack:
                print(i)
            return True
        # 四个方向x,y  x-1,y; x+1,y; x,y-1, ;x,y+1
        for dir in dirs:
            next_node = dir(cur_node[0], cur_node[1])
            # 如果下个节点能走
            if matrix[next_node[0]][next_node[1]] == 0:
                stack.append(next_node)
                matrix[next_node[0]][next_node[1]] = 2  # 做标记  表示已经走过
                break
        else:
            matrix[cur_node[0]][cur_node[1]] = 2
            stack.pop()
    print('没有路')
    return False


from collections import deque


# 队列 - 广度优先
def maze_path_queue(x1, y1, x2, y2):
    path = [[], []]  # 队列替换路径 [点位， 替换点位的索引]
    queue = deque()
    # queue = []  # 先进先出
    queue.append((x1, y1))
    path[0].append((x1, y1))
    path[1].append(-1)

    def search_path(node):
        print(node)
        previous_index = path[1][path[0].index(node)]
        if previous_index != -1:
            node = path[0][previous_index]
            search_path(node)

    while queue:
        # print(queue)
        # 先出队
        # cur_node = queue.pop(0)
        cur_node = queue.popleft()
        if cur_node[0] == x2 and cur_node[1] == y2:
            search_path(cur_node)
            return
        for dir in dirs:
            next_node = dir(cur_node[0], cur_node[1])
            if matrix[next_node[0]][next_node[1]] == 0:
                path[0].append(next_node)
                path[1].append(path[0].index(cur_node))
                queue.append(next_node)
                matrix[next_node[0]][next_node[1]] = 2
    print('没有路啊')
    return


if __name__ == '__main__':
    maze_path_queue(1, 1, 5, 5)
