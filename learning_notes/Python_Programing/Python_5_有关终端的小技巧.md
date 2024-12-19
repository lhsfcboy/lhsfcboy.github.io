# Python与系统终端

## 终端绘制基础图

$ pip install bashplotlib

## 终止程序的运行

```python
exit()
quit()
import sys
sys.exit()
```

## 清屏

```python
    os.system('cls' if os.name == 'nt' else 'clear')
```
