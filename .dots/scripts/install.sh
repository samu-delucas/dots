#!/bin/bash
#
# .dots/scripts/install.sh
# 
# Clone the repository and set up the proper paths for the programs

# Cloning the repository

# 1. Avoid recursion errors
echo ".dotscfg" >> .gitignore
# 2. Clone the repo
git clone https://github.com/samu-delucas/dots.git $HOME/.dotscfg
# 3. Set an alias for this session (the same alias is included in ~/.dots/shell/.aliasrc)
alias dotscfg='/usr/bin/git --git-dir=$HOME/.dotscfg/.git --work-tree=$HOME'
# 4. Don't show untracked files (we only want to track the ones that we add)
config config --local status.showUntrackedFiles no
# 5. Get the actual files (I think lol)
config checkout

# Setting paths
sudo echo "export ZDOTDIR=$HOME/.dots/shell/zsh" >> /etc/zsh/zshenv
