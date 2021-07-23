# 
# $ZDOTDIR/.zshrc
#
# Main config file, only for my user
#

# Lines configured by zsh-newuser-install
HISTFILE=$ZDOTDIR/.zsh_history
HISTSIZE=20000
SAVEHIST=20000
bindkey -v
# End of lines configured by zsh-newuser-install

# Lines configured by ME

# Source some files checking their existance
if [[ -r $ZDOTDIR/.zsh_completition ]]; then
    source $ZDOTDIR/.zsh_completition
fi

if [[ -r $ZDOTDIR/../aliases.sh ]]; then
    source $ZDOTDIR/../aliases.sh
fi

if [[ -r $ZDOTDIR/theme ]]; then
    source $ZDOTDIR/theme
fi

# End of lines configured by ME
