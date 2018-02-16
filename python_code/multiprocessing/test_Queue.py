<<<<<<< HEAD
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
=======
from multiprocessing import Process
import os
import random
import collections
import time
from pprint import pprint
import sys

ChildOrder = collections.namedtuple('ChildOrder', 'id status amount')




def run_proc(child_order_list):
    print('Run child process (%s)...' % (os.getpid()))
    while True:
        time.sleep(3)
        print("print from sub process")
        print(child_order_list)
        for childorder in child_order_list:
            print(childorder)
            sys.exit()
            if childorder.status == "new":
                print("Found a new order")

child_order_list = []
if __name__ == '__main__':
    

    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=(child_order_list,))
    print('Child process will start.')
    p.start()

    while True:
        time.sleep(2)
        new_child_order = ChildOrder(id=int(time.time()), status="new", amount=10)
        child_order_list.append(new_child_order)
        print("print from mian process")
        pprint(child_order_list)
        print()
>>>>>>> dc12fd2a3d453a8d7a6becd70e46be1b45396377
