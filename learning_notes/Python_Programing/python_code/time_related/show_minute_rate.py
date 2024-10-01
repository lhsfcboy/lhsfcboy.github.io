#!/bin/env python
import time
import random
ts_list = []

while True:
    time.sleep(random.random())

    current_ts = time.time()
    ts_list.append(current_ts)

    ts_list = [x for x in ts_list if x > current_ts-10]
    print(f"\rIn last minute, we have {len(ts_list)}", end='')
