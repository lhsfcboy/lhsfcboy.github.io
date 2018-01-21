import time;

ts = time.time()
print(ts)
print("1234567890.1234567")
import datetime;

ts = datetime.datetime.now().timestamp()
print(ts)
print("1234567890.1234567")

import calendar;
import time;

ts = calendar.timegm(time.gmtime())
print(ts)
