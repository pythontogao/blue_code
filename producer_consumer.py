from multiprocessing import Process, Queue
import time
import random
import os


def consumer(q):
    while 1:
        res = q.get()
        if res is None:  # 收到信号就结束
            break
        time.sleep(random.randint(2, 5))
        print('\033[31m%s消耗了%s\033[0m' % (os.getpid(), res))


def producer(q):
    for i in range(10):
        time.sleep(random.randint(1, 3))
        res = "食物%s" % i
        q.put(res)
        print('\033[32m%s生产了%s\033[0m' % (os.getpid(), res))


if __name__ == '__main__':
    q = Queue()
    p = Process(target=producer, args=(q,))
    c = Process(target=consumer, args=(q,))
    p.start()
    c.start()

    p.join()
    q.put(None)  # for结束后发信号
    print("主进程结束")
