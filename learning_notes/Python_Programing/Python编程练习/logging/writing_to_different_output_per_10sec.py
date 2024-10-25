#!/bin/env python

import time

last_mins = int(time.time()//10)

while True:
    filename = f"dummy_{last_mins}.log"
    with open(filename, "a") as f:
        while True:
            time.sleep(1)
            f.write(str(time.time())+"\n")
            print(str(time.time())+"\t"+filename)
            current_mins = int(time.time()//10)
            if current_mins > last_mins:
                last_mins = current_mins
                break
