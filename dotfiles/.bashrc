# echo "called .bashrc"

# User specific aliases and functions
alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'
alias vi='vim'
alias cls='clear'
alias ls='ls --color=auto'

# git related aliases
alias gs='git status'
alias shg='git pull;git add -A; git commit -m "`date +"%F%t%T"` Daily Commit";git push;'



## export CLICOLOR=1
## export LSCOLORS=dxfxcxdxbxegedabagacad


# Source global definitions
if [ -f /etc/bashrc ]; then
    . /etc/bashrc
fi

### python path
#export PATH=/usr/local/bin:$PATH
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python2.7
export PIP_REQUIRE_VIRTUALENV=true

export WORKON_HOME=$HOME/.virtualenvs
source /usr/bin/virtualenvwrapper.sh

workon p35

# terminal color setup
export TERM=xterm-256color
force_color_prompt=yes

### history command
export HISTTIMEFORMAT="%Y%m%d-%H:%M:%S "
export HISTFILESIZE=500000000
export HISTSIZE=1000000
export HISTCONTROL=ignoredups
PROMPT_COMMAND='history -a'


export EDITOR=vim
