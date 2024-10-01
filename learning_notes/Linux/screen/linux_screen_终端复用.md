
## 参考

- [IBM: 使用 screen 管理你的远程会话](https://www.ibm.com/developerworks/cn/linux/l-cn-screen/index.html)
- [Screen User’s Manual](https://www.gnu.org/software/screen/manual/screen.html)
## 安装与版本检查
    apt-get -y install screen
    yum -y install screen
    
    
    rpm -qa|grep screen
    screen -v

## 开始使用Screen

    screen #新建并进入一个不具名screen会话的窗口
    screen -S name #新建并进入一个名为name的screen会话的窗口
    screen -dmS test1    # 创建一个screen会话,并且不连入,名字是test1
    screen -r test1    # 连入指定会话
    screen vi test.c #新建并进入一个不具名screen会话的窗口, 并执行命令
    screen -ls #查看现有会话
    # 可以通过kill -9 9348杀死该会话，然后通过screen -wipe清理被杀死的会话
    
    screen -r xxxx #连接到名为xxxx, 或screen_pid为xxxx的会话
    C-a, c #在当前会话内生成一个新的窗口并切换到该窗口
    C-a, d #中断当前会话, 先按下Ctr+a然后按d键 
    
## 分屏
    C-a, S-s #上下分屏
    C-a, Tab #切换屏幕
    C-a, c   #创建新的终端
    C-a, x   #关闭终端, 也就是exit
    C-a, "   #显示当前Screen里的所有bash窗口，并可以进行选择

## 常用的键绑定

    C-a ?	显示所有键绑定信息
    C-a w	显示所有窗口列表
    C-a C-a	切换到之前显示的窗口
    C-a c	创建一个新的运行shell的窗口并切换到该窗口
    C-a n	切换到下一个窗口
    C-a p	切换到前一个窗口(与C-a n相对)
    C-a 0..9	切换到窗口0..9
    C-a a	发送 C-a到当前窗口
    C-a d	暂时断开screen会话
    C-a k	杀掉当前窗口
    C-a [	进入拷贝/回滚模式


    C-a c      创建新bash窗口，
    C-a k      删除当前的窗口，
    C-a A      为当前bash窗口设定一个标题，
    C-a C-z    挂起终端，也就是可以用jobs,fg之类的命令管理

    Ctrl-a S         新建水平分割窗口
    Ctrl-a Tab       切换窗口
    Ctrl-a X         关闭当前窗口

    Ctrl-a <Esc> 进入选择模式
    <PageUp> 或 Ctrl-u 光标上移一页
    <PageDown> 或 Ctrl-d 光标下移一页 
    <Left> 或 h 光标左移一格
    <Down> 或 j 光标下移一行
    <Up> 或 k 光标上移一行
    <Right> 或 l 光标右移一格
    <Space> 选择开始，选择结束
    <Esc> 退出选择模式

    Ctrl-a ] 粘贴选择的内容
