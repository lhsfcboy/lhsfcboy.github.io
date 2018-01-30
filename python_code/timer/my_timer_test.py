import time
import random


min_interval = 1/2

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