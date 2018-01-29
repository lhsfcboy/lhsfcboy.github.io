import logging
import time
from time import sleep

#logging.basicConfig(level=logging.INFO,format="%(levelname)s:%(asctime)s:%(created)f:%(msecs)d:%(relativeCreated)d:%(message)s")
logging.basicConfig(level=logging.INFO,filename='example.log',format="%(asctime)s.%(msecs)03d[%(levelname)-8s]:%(created).6f %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

logging.error("出现了错误")
sleep(1)
logging.info("bs_amount_ratio is 1.834679120207966")
sleep(1)
logging.warning("警告信息")
sleep(1)
logging.critical ("critical")



import imported_module
while True:
    sleep(0.2)
    logging.info("buy order issued")