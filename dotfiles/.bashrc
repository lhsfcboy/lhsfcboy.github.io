# .bashrc

#echo "called .bashrc"
# User specific aliases and functions

alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'
alias vi='vim'


alias gs='git status'
alias shg='git pull;git add -A; git commit -m "`date +"%F%t%T"` Daily Commit";git push;'
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

workon p36

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
