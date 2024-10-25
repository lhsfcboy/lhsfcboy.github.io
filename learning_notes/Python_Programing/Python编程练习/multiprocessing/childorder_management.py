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