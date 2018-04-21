ls ~/.bash_profile


alias gs="git status"

alias ls='ls --show-control-chars'    # 避免日语乱码


Git for Windows のインストーラでそのまま入れると大体は"C:\Program Files(x86)\Git\bin\"にある"vim"を編集します。


vim ~/.gitconfig

[core]
        editor = /C/vim/gvim --nofork -c 'set fenc=utf-8' +1