alias ls='ls --color=auto'
alias la='ls -a'
alias ll='ls -la'
alias grep='grep --color=auto'
alias g='git'
alias ga='git add'
alias gc='git commit -m'
alias gp='git push'
alias .git='/usr/bin/git --git-dir=$HOME/.dotsrepo/ --work-tree=$HOME'
alias vim='nvim'
alias pacman='sudo pacman --color=auto'

# Use $XINITRC variable if file exists
[ -f "$XINITRC" ] && alias startx="startx $XINITRC"
