import os
import random
import time
from multiprocessing import Process, Queue
from multiprocessing import Manager



def execution_watch(q):
    # 检查现有的open中的订单, 并更新其信息
    print(f'Run child process execution_watch on pid {os.getpid()}...')
    while True:
        print("Start to check")
        for item in q:
            if item >= 10:
                q.remove(item)
        time.sleep(2)
        print("Check is over.")

if __name__ == '__main__': 
    q=Manager().list()
    
    execution_watch_process = Process(target=execution_watch, args=(q,))
    execution_watch_process.start()


    print("Hello, I will put something to q.")
    while True:
        value = random.randint(1, 20)
        print('Put %s to q...' % value)
        q.append(value)
        print(q)
        time.sleep(1)
