# Tmux 快捷键 & 速查表

## 学习教程
- [Tmux 使用教程 作者： 阮一峰](https://www.ruanyifeng.com/blog/2019/10/tmux.html)
- [Tmux使用手册](http://louiszhai.github.io/2017/09/30/tmux/#Tmux%E4%BC%98%E5%8C%96)  


## 创建会话Session 与使用退出

```bash
#启动新会话：
tmux [new -s 会话名 -n 窗口名]
tmux new -s sessionname
tmux new -s sessionname -d #在后台建立会话

tmux ls
tmux attach -t sessionnmae
tmux attach #进入最近的tmux的session

ctrl+b d #脱离当前会话

tmux kill-session -t 会话名 #关闭会话
```

## 窗口操作

```bash
ctrl+b c #创建新窗口
ctrl+b n #选择下一个窗口
ctrl+b l #最后使用的窗口
ctrl+b p #选择前一个窗口
ctrl+b w #以菜单方式显示及选择窗口
```

关闭所有会话：

```console
    tmux ls | grep : | cut -d. -f1 | awk '{print substr($1, 0, length($1)-1)}' | xargs kill
```

 在 Tmux 中，按下 Tmux 前缀 `ctrl+b`，然后：

## 会话（Session）

    :new<回车>  启动新会话
    s           列出所有会话
    $           重命名当前会话

## 窗口()

    c  创建新窗口
    w  列出所有窗口
    n  后一个窗口
    p  前一个窗口
    0~9 选择0~9对应的窗口
    f  查找窗口
    ,  重命名当前窗口
    &  关闭当前窗口

## 调整窗口排序

    swap-window -s 3 -t 1  交换 3 号和 1 号窗口
    swap-window -t 1       交换当前和 1 号窗口
    move-window -t 1       移动当前窗口到 1 号

## 窗格(Panel)
我们可以进一步分割窗口为窗格

    %  垂直分割/创建一个水平窗格
    "  水平分割/创建一个竖直窗格
    o  交换窗格
    x  关闭窗格
    ⍽  左边这个符号代表空格键 - 切换布局
    q 显示每个窗格是第几个，当数字出现的时候按数字几就选中第几个窗格
    { 与上一个窗格交换位置
    } 与下一个窗格交换位置
    z 切换窗格最大化/最小化
    ! 在新窗口中显示当前窗格
    t 在当前窗格显示时间

## 同步窗格

这么做可以切换到想要的窗口，输入 Tmux 前缀和一个冒号呼出命令提示行，然后输入：

```
:setw synchronize-panes
```

你可以指定开或关，否则重复执行命令会在两者间切换。
这个选项值针对某个窗口有效，不会影响别的会话和窗口。
完事儿之后再次执行命令来关闭。[查看](http://blog.sanctum.geek.nz/sync-tmux-panes/)


## 调整窗格尺寸

如果你不喜欢默认布局，可以重调窗格的尺寸。虽然这很容易实现，但一般不需要这么干。这几个命令用来调整窗格：

    PREFIX : resize-pane -D          当前窗格向下扩大 1 格
    PREFIX : resize-pane -U          当前窗格向上扩大 1 格
    PREFIX : resize-pane -L          当前窗格向左扩大 1 格
    PREFIX : resize-pane -R          当前窗格向右扩大 1 格
    PREFIX : resize-pane -D 20       当前窗格向下扩大 20 格
    PREFIX : resize-pane -t 2 -L 20  编号为 2 的窗格向左扩大 20 格


## 文本复制模式：

按下**前缀 [**进入文本复制模式。可以使用方向键在屏幕中移动光标。默认情况下，方向键是启用的。在配置文件中启用 Vim 键盘布局来切换窗口、调整窗格大小。Tmux 也支持 Vi 模式。要是想启用 Vi 模式，只需要把下面这一行添加到 .tmux.conf 中：

    setw -g mode-keys vi

启用这条配置后，就可以使用 h、j、k、l 来移动光标了。

想要退出文本复制模式的话，按下回车键就可以了。一次移动一格效率低下，在 Vi 模式启用的情况下，可以辅助一些别的快捷键高效工作。

例如，可以使用 w 键逐词移动，使用 b 键逐词回退。使用 f 键加上任意字符跳转到当前行第一次出现该字符的位置，使用 F 键达到相反的效果。

    vi             emacs        功能
    ^              M-m          反缩进
    Escape         C-g          清除选定内容
    Enter          M-w          复制选定内容
    j              Down         光标下移
    h              Left         光标左移
    l              Right        光标右移
    L                           光标移到尾行
    M              M-r          光标移到中间行
    H              M-R          光标移到首行
    k              Up           光标上移
    d              C-u          删除整行
    D              C-k          删除到行末
    $              C-e          移到行尾
    :              g            前往指定行
    C-d            M-Down       向下滚动半屏
    C-u            M-Up         向上滚动半屏
    C-f            Page down    下一页
    w              M-f          下一个词
    p              C-y          粘贴
    C-b            Page up      上一页
    b              M-b          上一个词
    q              Escape       退出
    C-Down or J    C-Down       向下翻
    C-Up or K      C-Up         向下翻
    n              n            继续搜索
    ?              C-r          向前搜索
    /              C-s          向后搜索
    0              C-a          移到行首
    Space          C-Space      开始选中
                   C-t          字符调序

## 杂项：

    d  退出 tmux（tmux 仍在后台运行）
    t  窗口中央显示一个数字时钟
    ?  列出所有快捷键
    :  命令提示符

## 配置选项：

    # 鼠标支持 - 设置为 on 来启用鼠标
    * setw -g mode-mouse off
    * set -g mouse-select-pane off
    * set -g mouse-resize-pane off
    * set -g mouse-select-window off

    # 设置默认终端模式为 256color
    set -g default-terminal "screen-256color"

    # 启用活动警告
    setw -g monitor-activity on
    set -g visual-activity on

    # 居中窗口列表
    set -g status-justify centre

    # 最大化/恢复窗格
    unbind Up bind Up new-window -d -n tmp \; swap-pane -s tmp.1 \; select-window -t tmp
    unbind Down
    bind Down last-window \; swap-pane -s tmp.1 \; kill-window -t tmp

## 配置文件（~/.tmux.conf）：

```bash
# 基础设置
set -g default-terminal "screen-256color"
set -g display-time 3000
set -g escape-time 0
set -g history-limit 65535
set -g base-index 1
set -g pane-base-index 1

# 前缀绑定 (Ctrl+a)
set -g prefix ^a
unbind ^b
bind a send-prefix

# 分割窗口
unbind '"'
bind - splitw -v
unbind %
bind | splitw -h

# 选中窗口
bind-key k select-pane -U
bind-key j select-pane -D
bind-key h select-pane -L
bind-key l select-pane -R

# copy-mode 将快捷键设置为 vi 模式
setw -g mode-keys vi

# 启用鼠标(Tmux v2.1)
set -g mouse on

# 更新配置文件
bind r source-file ~/.tmux.conf \; display "已更新"

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Tmux Plugin Manager(Tmux v2.1)
# Tmux Resurrect
set -g @plugin 'tmux-plugins/tmux-resurrect'

# List of plugins
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-sensible'

# Other examples:
# set -g @plugin 'github_username/plugin_name'
# set -g @plugin 'git@github.com/user/plugin'
# set -g @plugin 'git@bitbucket.com/user/plugin'

# Initialize TMUX plugin manager (keep this line at the very bottom of tmux.conf)
run '~/.tmux/plugins/tpm/tpm'
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

```
