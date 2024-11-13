## Vim-Vi IMproved

Vim是从vi发展出来的一个文本编辑器。代码补全、编译及错误跳转等方便编程的功能特别丰富，在程序员中被广泛使用。开始学习的时候可能会进展缓慢，但是一旦掌握一些基本操作之后，能大幅度提高编辑效率。
Linux操作系统自带的编辑器。需要远程登陆到主机上临时操作的时候很方便，有时也是唯一的选择。

Vim特别适合对与现有的工程文件浏览，定位，进行细微的变动。比如修正Typo，调整参数等。

- [简明 Vim 练级攻略 作者： 左耳朵耗子](http://coolshell.cn/articles/5426.html)
- [Vim 配置入门 作者： 阮一峰](https://www.ruanyifeng.com/blog/2018/09/vimrc.html)

- 作者： 阮一峰
注意我们学习的目的：
- 需要学会最基本的操作
  - 不追求vim的高级操作技巧
- 避免使用插件
  - 远程登录的主机通常都无法自由安装插件
  - 搜索 “vim无插件编程” ，这可以视为我们学习的终点

## 无插件vim配置   

- https://github.com/wklken/vim-for-server
- 

## 外观

Use `:color molokai` to switch to a color scheme.

vim不同关键字字体颜色修改方法

```vimrc
" 修改字符串颜色
hi Comment ctermfg =blue
" 修改字符串颜色
hi String ctermfg =darkred
" 修改类型颜色
hi Type ctermfg =yellow
" 修改数字颜色
hi Number ctermfg =darkblue
" 修改常量颜色
hi Constant ctermfg =blue
" 修改声明颜色
hi Statement ctermfg =darkyellow
```
## 配置候选
```vim
" 参考资料
“ http://www.cnblogs.com/ma6174/archive/2011/12/10/2283393.html
“ http://blog.sina.com.cn/s/blog_5ca785c30100dk6x.html
“ http://tech.ddvip.com/2013-08/1375715872200336.html
“ http://www.douban.com/note/233264337/



""""""""""""""""""""""""""""""""""""""""""""""""""
"新文件标题
""""""""""""""""""""""""""""""""""""""""""""""""""
"新建.sh,.c,.cpp,.h,.java,.py文件,自动插入文件头,
autocmd BufNewFile *.sh,*.c,*.cpp,*.java,*.py exec ":call SetTitle()"
"定义函数SetTitle,自动插入头文件
func SetTitle()
    "如果文件类型为.sh文件
    if &filetype == 'sh' 
        call setline(1,"\##################################################") 
        call append(line("."), "\# File Name: ".expand("%")) 
        call append(line(".")+1, "\# Author: TomatoFish") 
        call append(line(".")+2, "\# mail: 2545593890@qq.com") 
        call append(line(".")+3, "\# Created Time: ".strftime("%Y-%m-%d/%H:%M:%S")."")
        call append(line(".")+4, "\##################################################") 
        call append(line(".")+5, "\#!/bin/bash") 
        call append(line(".")+6, "") 
    else 
        call setline(1, "/**************************************************") 
        call append(line("."), "* File Name: ".expand("%")) 
        call append(line(".")+1, "* Author: TomatoFish") 
        call append(line(".")+2, "* Mail: 2545593890@qq.com") 
        call append(line(".")+3, "* Created Time: ".strftime("%Y-%m-%d/%H:%M:%S")."")
        call append(line(".")+4, "**************************************************/") 
        call append(line(".")+5, "")
    endif
 
    if &filetype == 'c'
        call append(line(".")+6, "#include <stdio.h>")
        call append(line(".")+7, "#include <stdlib.h>")
        call append(line(".")+8, "#include <string.h>")
        call append(line(".")+9, "")
        call append(line(".")+10, "int main()")
        call append(line(".")+11, "{")
        call append(line(".")+12, "    ")
        call append(line(".")+13, "    return 0;")
        call append(line(".")+14, "}")
    endif
 
    if &filetype == 'cpp'
        call append(line(".")+6, "#include <cstdio>")
        call append(line(".")+7, "#include <cstdlib>")
        call append(line(".")+8, "#include <cstring>")
        call append(line(".")+9, "#include <cmath>")
        call append(line(".")+10, "#include <iostream>")
        call append(line(".")+11, "#include <algorithm>")
        call append(line(".")+12, "using namespace std;")
        call append(line(".")+13, "")
        call append(line(".")+14, "int main()")
        call append(line(".")+15, "{")
        call append(line(".")+16, "    ")
        call append(line(".")+17, "    return 0;")
        call append(line(".")+18, "}")
    endif
 
    if &filetype == 'java'
    endif
 
    if &filetype == 'py'
    endif
 
    "新建文件后,自动定位到文件末尾
    autocmd BufNewFile * normal G
endfunc
 
 
""""""""""""""""""""""""""""""""""""""""""""""""""
"编译运行调试
""""""""""""""""""""""""""""""""""""""""""""""""""
"sh,c,cpp,java,py 按F5编译运行
map <F5> :call CompileRunGcc()<CR>
func! CompileRunGcc()
    exec "w"
    if &filetype == 'sh'
        :!./%
    elseif &filetype == 'c'
        exec "!gcc % -o %< -lm"
        exec "! ./%<"
    elseif &filetype == 'cpp'
        exec "!g++ % -o %< -lm"
        exec "! ./%<"
    elseif &filetype == 'java'
        exec "!javac %"
        exec "!java %<"
    elseif &filetype == 'py'
        exec "!python %<"
    endif
endfunc
 
"C,C++的调试
map <F8> :call Rungdb()<CR>
func! Rungdb()
    exec "w"
    exec "!g++ % -g -o %< -lm"
    exec "!gdb ./%<"
endfunc


""""""""""""""""""""""""""""""""""""""""""""""""""
"基本设置
""""""""""""""""""""""""""""""""""""""""""""""""""
filetype on  "开启文件类型侦测
"根据侦测到的不同类型加载对应的插件
filetype plugin on
"开启实时搜索功能
set incsearch
"搜索时大小写不敏感
set ignorecase
"关闭兼容(vi)模式
set nocompatible
"vim自身命令行模式智能补全
set wildmenu
"与系统共享剪贴板
"set clipboard+=unnamed    "ubuntu下貌似没用
map <C-c> "+y    "先sudo apt-get install vim-gnome,设置快捷键ctrl+c
map <C-v> "+p    "先sudo apt-get install vim-gnome,设置快捷键ctrl+v
 
"历史记录数
set history=1000
 
"禁止生成临时文件
set nobackup
set noswapfile
 
 
 
""""""""""""""""""""""""""""""""""""""""""""""""""
"界面美化
""""""""""""""""""""""""""""""""""""""""""""""""""
"主体风格
"配色方案
set background=dark
"colorscheme solarized
"colorscheme molokai
colorscheme phd
 
 
"营造专注氛围
"禁止光标闪烁
set gcr=a:block-blinkon0
 
"禁止显示滚动条
set guioptions-=l
set guioptions-=L
set guioptions-=r
set guioptions-=R
 
"禁止显示菜单和工具条
set guioptions-=m
set guioptions-=T
 
"启动的时候不显示援助乌干达儿童的提示
"set shortmess=atI
 
"去掉输入错误的提示声音
set noeb
 
 
"添加辅助信息
"总是显示状态栏
set laststatus=2
 
"显示光标当前位置
set ruler
 
"开启行号显示
set number
 
"高亮显示当前行/列
set cursorline
set cursorcolumn
 
"高亮显示搜索结果
set hlsearch
set incsearch
 
 
"其他美化
"禁止折行
set nowrap
 
" 设置配色方案
"colorscheme murphy
set fencs=utf-8,ucs-bom,shift-jis,gb18030,gbk,gb2312,cp936
set termencoding=utf-8
set encoding=utf-8
set fileencodings=ucs-bom,utf-8,cp936
set fileencoding=utf-8
 
""""""""""""""""""""""""""""""""""""""""""""""""""
"代码分析
""""""""""""""""""""""""""""""""""""""""""""""""""
"语法高亮
"开启语法高亮功能
syntax enable
 
"允许用指定语法高亮配色方案替换默认方案
syntax on
 
 
"代码缩进
"自适应不同语言的智能缩进
filetype indent on
 
"将制表符扩展为空格
set expandtab
 
"设置编辑时制表符占用空格数
set tabstop=4
 
"设置格式化时制表符占用空格数
set shiftwidth=4
 
"让vim吧连续数量的空格视为一个制表符
set softtabstop=4
 
"在行和段开始处使用制表符
set smarttab
 
"代码折叠
"允许折叠
set foldenable
 
"手动折叠
set foldmethod=manual
 
"基于缩进或语法进行代码折叠
set foldmethod=indent
set foldmethod=syntax
 
"启动vim时关闭折叠代码
set nofoldenable
 
 
 
""""""""""""""""""""""""""""""""""""""""""""""""""
"代码开发
"""""""""""""""""""""""""""""""""""""""""""""""""





```
