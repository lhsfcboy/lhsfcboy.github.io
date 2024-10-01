import logging
from time import sleep


logging.error("Logging from imported module! error")
sleep(1)
logging.info("Logging from imported module! info")
sleep(1)
logging.warning("Logging from imported module! warning")
sleep(1)
logging.critical("Logging from imported module! critical")