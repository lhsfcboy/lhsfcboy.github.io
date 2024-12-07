# Python 性能分析

## 简单的性能分析

### 使用 `cProfile` 模块进行性能分析

运行 Python 脚本并按累计时间排序函数的性能分析：

```bash
python -m cProfile -s cumulative demo01.py
```

生成性能统计文件并使用 `pstats` 模块进行详细分析：

```bash
python -m cProfile -o profile.stats demo01.py
```

### 使用 `pstats` 进行分析

加载统计文件并进行分析：

```python
import pstats

p = pstats.Stats('profile.stats')
# 按累计时间排序
p.sort_stats("cumulative")
# 输出累计时间报告
p.print_stats()
# 输出调用者的信息
p.print_callers()
# 输出哪个函数调用了哪个函数
p.print_callees()
```

### 使用交互式页面查看性能分析

通过交互式界面分析统计结果：

```bash
python -m pstats profile.stats
```

交互式命令：

- 去掉冗长的文件路径：

  ```bash
  % strip
  ```

- 查看排序选项：

  ```bash
  % sort
  ```

- 按累计时间排序并查看前 5 条结果：

  ```bash
  % sort cumulative
  % stats 5
  ```

- 退出交互模式：

  ```bash
  % quit
  ```

### 性能分析报告的可视化

安装所需工具：

```bash
yum install graphviz -y  # 提供 `dot` 命令
pip install gprof2dot
```

生成可视化性能分析报告：

```bash
gprof2dot -f pstats profile.stats | dot -Tpng -o profile.png
```

- 在生成的图中，顺着浅色方格查看，可以快速发现程序的瓶颈。

### 其他性能分析工具

更多工具参考：[Python 性能分析工具总结](http://python.jobbole.com/87621/)
