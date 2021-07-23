
alias sudo='sudo '

alias ls='ls --color=auto'
alias la='ls -A'
alias ll='ls -lA'

alias grep='grep --color=auto'

alias g='git'
alias ga='git add'
alias gc='git commit -m'
alias gp='git push'
alias .git='/usr/bin/git --git-dir=$HOME/.dotsrepo/ --work-tree=$HOME'

alias vim='nvim'

alias pacman='sudo pacman --color=auto'
alias trizen='trizen --color=auto --noedit'
alias syu='pacman -Syu'
alias tsyu='\trizen -Syu'
alias sp='\trizen -Ss --color=auto'

alias vpnuam='sudo vpnc uam'
alias vpnuamoff='sudo vpnc-disconnect'

# DOESN'T WORK PROPERLY
# Clear and reset wont have \n on the top of the terminal
# alias clear='NEW_LINE_BEFORE_PROMPT=0;clear'
# alias reset='NEW_LINE_BEFORE_PROMPT=0;reset' #redundant, reset uses clear

# Use $XINITRC variable if file exists
[ -f "$XINITRC" ] && alias startx="startx $XINITRC"
