from retry import retry
from retry.api import retry_call
from random import randint
import time


#@retry(tries=13,delay=1)
def make_trouble():

    if randint(0,9) != 5:
        print(f"\tIn trouble!")
        raise Exception
    else:
        print("Another good day!",time.strftime("%X"))

for i in range(10):
    retry_call(make_trouble,tries=10,delay=1)

