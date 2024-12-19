# Python 时间处理

## datetime 与 date

除非非常明确不处理日期以外的数据, 否则,统一使用datetime

不允许import datetime, 必须
from datetime import datetime, date, time, timedelta

除非明确使用time包中sleep以外的方法, 否则不直接引入time,
from time import sleep
