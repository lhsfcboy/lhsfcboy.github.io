ls ~/.bash_profile


alias gs="git status"

alias ls='ls --show-control-chars'    # 避免日语乱码


Git for Windows のインストーラでそのまま入れると大体は"C:\Program Files(x86)\Git\bin\"にある"vim"を編集します。


vim ~/.gitconfig

[core]
        editor = /C/vim/gvim --nofork -c 'set fenc=utf-8' +1
        
        
### 修改GitBash的提示符(prompt)

使用管理员权限修改文件: `C:\Program Files\Git\etc\profile.d\git-prompt.sh`