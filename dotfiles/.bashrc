# .bashrc

#echo "called .bashrc"

# Git on Windows
if [ -z "$HOMEDRIVE" ]
then
    ## if on Linux

    #echo "not a gitbash console"

    ### python path
    #export PATH=/usr/local/bin:$PATH

    export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python2.7
    export PIP_REQUIRE_VIRTUALENV=true
    export WORKON_HOME=$HOME/.virtualenvs
    source /usr/bin/virtualenvwrapper.sh

    workon p36
else
    ## if on Windows

    cd /D/GitHubWorkSpace/

    alias myd='cd /D/GitHubWorkSpace/'
    alias python='winpty python.exe'
    export PYTHONIOENCODING=UTF-8
fi

# User specific aliases and functions

# alias
alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'
alias vi='vim'
alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

alias rrm='/bin/rm -rf'
# alias rm='mv --target-directory ~/.trash'


# git related
alias gs='git status'
alias shg='git pull;git add -A; git commit -m "`date +"%F%t%T"` Daily Commit";git push;'
# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

export TERM=xterm-256color
force_color_prompt=yes



### history command

export HISTTIMEFORMAT="%Y%m%d-%H:%M:%S "
export HISTFILESIZE=500000000
export HISTSIZE=1000000
export HISTCONTROL=ignoredups
PROMPT_COMMAND='history -a'

export CLASSPATH=/root/temp/Algorithms_4th/lib/algs4.jar:$CLASSPATH

export EDITOR=vim
