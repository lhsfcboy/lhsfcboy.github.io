import time
from time import sleep
import random
import logging
logging.basicConfig(level=logging.INFO,format="%(asctime)s.%(msecs)03d[%(levelname)-8s]:%(created).6f %(message)s", datefmt="%Y-%m-%d %H:%M:%S")


min_interval = 1/2


while True:
    # 对齐到每分钟第45秒
    sleep(60-(int(time.time())-45) % 60)
    logging.info(f"Running heavy job, may cost 5 to 15 seconds")
    task_time = random.randint(5,15)
    logging.info(f"This time, it will take {task_time} seconds")
    sleep(task_time)


while True:
	task_start_ts = time.time()
	time.sleep(random.random())
	task_end_ts = time.time()
	task_ts_delta = task_end_ts - task_start_ts
	print(f"Task run for {task_ts_delta}")
	if task_ts_delta < min_interval:
		pad_time = min_interval - task_ts_delta
		time.sleep(min_interval - task_ts_delta)
		print(f"pad_time is {pad_time}")
	print(f"\t\t\tTask time with sleep is {time.time()-task_start_ts}")


print(time.time())