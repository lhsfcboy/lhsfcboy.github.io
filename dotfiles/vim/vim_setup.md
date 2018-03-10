vim的配置

# 通用篇

## 安装

### 安装vim
```
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
```
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
```

## F5 快速编译执行

```

aaa
```

## 代码补全

效果: ifmain[Tab] 
```
    if __name__ == '__main__':
        main()
```

logf[Tab]
```
loggging.info(f"{}")
```





# python篇

## 编程提示(jedi-vim)

