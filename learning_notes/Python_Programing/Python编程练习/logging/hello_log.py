#!/usr/bin/env python
# encoding:UTF-8

from time import sleep
import random
import logging
logging.basicConfig(level=logging.INFO,format="%(asctime)s.%(msecs)03d[%(levelname)-8s]:%(created).6f %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

while True:
    sleep(15-(int(time.time())+2) % 15)
    logging.info(f"{int(time.time()) % 10}")

print("hello~")
logging.error("出现了错误")
sleep(1)
logging.info("bs_amount_ratio is 1.834679120207966")
sleep(1)
logging.warning("警告信息")
sleep(1)
logging.critical ("critical")
