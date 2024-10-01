#!/bin/env python

import time
from datetime import datetime

def get_date_int():
    datetime_obj = datetime.now()
    return datetime_obj.year * 10000 + datetime_obj.month * 100 + datetime_obj.day


last_mins = get_date_int()

while True:
    filename = f"dummy_{last_mins}.log"
    with open(filename, "a") as f:
        while True:
            time.sleep(1)
            f.write(str(time.time())+"\n")
            print(str(time.time())+"\t"+filename)
            current_mins = get_date_int()
            if current_mins > last_mins:
                last_mins = current_mins
                break
