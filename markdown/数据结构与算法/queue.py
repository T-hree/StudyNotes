# -- coding: utf-8 --

class Queue:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.queue = [0 for _ in range(maxsize)]
        self.rear = 0  # 队尾  只管插入
        self.front = 0  # 对头  只管删除

    def push(self, val):
        if self.is_full():
            print('队列已满')
            return
        self.queue[self.rear] = val
        self.rear = (self.rear + 1) % self.maxsize

    def pop(self):
        if self.is_empty():
            print('队列为空')
            return
        val, self.queue[self.front] = self.queue[self.front], 0
        self.front = (self.front + 1) % self.maxsize
        return val

    # 判断队空
    def is_empty(self):
        # # 判断队头有没有值
        # if self.queue[self.front]:
        #     return False
        # else:
        #     # 对头 无值 则空
        #     return True
        return self.front == self.rear

    # 判断堆满
    def is_full(self):
        # 判断队尾有没有值
        # if self.queue[self.rear]:
        #     # 队尾有值则满
        #     return True
        # else:
        #     return False
        # 什么条件队满  可以自定义
        # 少用一个元素空间，约定以“队列头指针front在队尾指针rear的下一个位置上”作为队列“满”状态的标志
        return (self.rear + 1) % self.maxsize == self.front


if __name__ == '__main__':
    queue = Queue(maxsize=5)

    # queue.pop()
    for i in range(1, 5):
        queue.push(i)
    print(queue.queue)
    print(queue.pop())
    print(queue.queue)
    queue.push(5)
    print(queue.queue)
    queue.push(6)
    print(queue.queue)
