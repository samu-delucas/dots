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

if [[ -r $ZDOTDIR/../.aliasrc ]]; then
    source $ZDOTDIR/../.aliasrc
fi

# End of lines configured by ME
