# .bashrc

#echo "called .bashrc"

# Git on Windows
if [ -z "$HOMEDRIVE" ]
then
    ## if on Linux

    #echo "not a gitbash console"

    if [[ -x `which colordiff` ]]; then
          alias diff='colordiff -u'
      else
          alias diff='diff -u'
    fi

    ### python path
    #export PATH=/usr/local/bin:$PATH
    PS1="[\D{%F %T} \u@\h:\w] \n$ "

    export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python2.7
    export PIP_REQUIRE_VIRTUALENV=true
    export WORKON_HOME=$HOME/.virtualenvs
    source /usr/bin/virtualenvwrapper.sh

    workon p36

    ### CentOS/RedHat alias
    alias install="sudo yum install -y"
    alias update="sudo yum update -y"
    alias upgrade="sudo yum upgrade -y"

else
    ## if on Windows
    alias myd='cd /D/GitHubWorkSpace/'
    alias cdg='cd /D/GitHubWorkSpace/'
    alias python='winpty python.exe'
    export PYTHONIOENCODING=UTF-8

    #cd /D/GitHubWorkSpace/

    if [ -z "$TMUX" ]
    then
        #echo "Not in tmux terminal"
        cd /D/GitHubWorkSpace/
    else
        true
    fi

    ### SSH
    alias myserver="ssh root@183.181.60.147"
fi

# User specific aliases and functions

# general alias
alias vi='vim'
alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'
alias mkdir='mkdir -pv' ## 自动创建父目录
alias rrm='/bin/rm -rf'
alias rmf='/bin/rm -f'
# alias rm='mv --target-directory ~/.trash'
# alias diff="diff --color=always" ## For diff later then v3.4
alias less="less -r"  ### keep color

alias ls='ls --color=auto'
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'

alias now='date +"%T"'
alias nowtime=now
alias nowdate='date +"%Y%m%d"'

alias cd..='cd ..'
alias ..='cd ..'
alias ...='cd ../../'
alias ....='cd ../../../'
alias .....='cd ../../../../'
alias .4='cd ../../../../'
alias .5='cd ../../../../..'

alias wget='wget -c' ## 默认打开断点续传

## system resource
## 系统资源

alias psmem='ps auxf | sort -nr -k 4'
alias psmem10='ps auxf | sort -nr -k 4 | head -10'
alias pscpu='ps auxf | sort -nr -k 3'
alias pscpu10='ps auxf | sort -nr -k 3 | head -10'

alias ports='netstat -tulanp'

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

######## END #########
