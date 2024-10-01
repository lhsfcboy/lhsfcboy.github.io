Reference   https://github.com/supasate/yosh

https://www.shiyanlou.com/courses/647/labs/2113/document

------------------------------------
|-- func/
|   |-- __init__.py
|   |-- cd.py
|   |-- constants.py
|   |-- exit.py
|   |-- getenv.py
|   `-- history.py
`-- shell.py

每个文件的作用如下：

shell.py ：Shell 的主程序，负责读取、解析并执行命令
func/ ：自定义模块，所有的自定义命令的实现函数文件都位于这里
__init__.py ：使 func 文件夹能作为 Python 模块被导入
cd.py ：实现了 Shell 的 cd 命令
constants.py ：定义了各种常量与路径
exit.py ：定义了 exit 命令，用来退出程序
getenv.py ：实现 getenv 命令，获取系统变量的值
history.py：实现 history 命令，展示输入的命令日志


Shell 的运行流程。

启动之后注册自定义的命令函数（即建立命令与相应函数的映射关系），输出命令提示符 $ ，等待用户输入命令；
用户输入命令之后按下回车，Shell 程序就要获取命令；
Shell 程序对命令格式进行解析；
解析之后，调用相关函数进行处理，如果当前命令的相关函数不存在则转交给系统处理，并将执行结果反馈给用户界面；
再次输出命令提示符 $ ，等待用户输入命令。
所以事实上，我们可以看出来从第五点开始就已经在重复第一点的功能了。因此 Shell 程序的主体应该放在一个 while 循环中，直到某一特定条件达成的时候，结束循环并退出程序。

比如，我们课程的做法就是设定变量 status 作为 while 循环的条件，当接收到 exit 命令的时候，执行 exit 函数，修改 status 的值为 0 从而退出程序。



