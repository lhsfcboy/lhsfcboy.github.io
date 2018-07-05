# vim的配置

通用篇

## 安装

### 安装vim

```concole
git clone git@github.com:vim/vim.git
cd vim/
./configure --with-features=huge \
            --enable-pythoninterp \
            --enable-rubyinterp \
            --enable-luainterp \
            --enable-perlinterp \
            --with-python-config-dir=/usr/lib/python2.7/config/ \
            --enable-gui=gtk2 \
            --enable-cscope \
            --prefix=/usr
make
make install
```

### 安装插件管理

```console
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
```

## F5 快速编译执行

```vim
"按F5一键编译并运行
map <F5> :call CompileRunGcc()<CR>
func! CompileRunGcc()
        exec "w"
        if &filetype == 'c'
           exec "!g++ % -DLOCAL -o   %<"
           exec "!time ./%<"
        elseif &filetype == 'cpp'
           exec "!g++ % -std=c++11 -DLOCAL -Dxiaoai -o    %<"
           exec "!time ./%<"
        elseif &filetype == 'java'
           exec "!javac %"
           exec "!time java %<"
        elseif &filetype == 'sh'
           :!time bash %
        elseif &filetype == 'python'
        exec "!time python %"
        endif
endfunc
```

## 代码补全

效果: ifmain[Tab]

```python
    if __name__ == '__main__':
        main()
```

logf[Tab]

```python
loggging.info(f"{}")
```

常见的代码补全插件

- snipMate
- xptemplate

## 语法检查 Syntastic

## python篇

## 编程提示(jedi-vim)

## 语法高亮

Use `:color molokai` to switch to a color scheme.
