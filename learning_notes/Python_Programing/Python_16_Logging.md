# Python Logging

- [Python Tutorial: Logging Basics - Logging to Files, Setting Levels, and Formatting](https://www.youtube.com/watch?v=-ARI4Cz-awo&list=WL&index=23)
- [Python Tutorial: Logging Advanced - Loggers, Handlers, and Formatters](https://www.youtube.com/watch?v=jxmzY9soFXg)

```python
import logging
logging.basicConfig(
level=logging.INFO,
format="%(asctime)s.%(msecs)03d[%(levelname)s]: %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)

logging.critical('critical')
logging.error('error')
logging.warning('warning')  #  by default
logging.info('info')
logging.debug('debug')
```

- DEBUG 最详细的日志信息，典型应用场景是 问题诊断
- INFO 信息详细程度仅次于DEBUG，通常只记录关键节点信息，用于确认一切都是按照我们预期的那样进行工作
- WARNING 当某些不期望的事情发生时记录的信息（如，磁盘可用空间较低），但是此时应用程序还是正常运行的
- ERROR 由于一个更严重的问题导致某些功能不能正常运行时记录的信息
- FATAL/CRITICAL 整个系统即将/完全崩溃
