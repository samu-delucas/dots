#!/bin/bash

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# .dots/scripts/install.sh
# 
# Clone the repository and set up the proper paths for the programs
# More info can be found on https://www.ackama.com/blog/posts/the-best-way-to-store-your-dotfiles-a-bare-git-repository-explained
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

### Cloning the repository
# 1. Avoid recursion errors
echo ".dotsrepo" >> .gitignore
# 2. Clone the repo
git clone --bare https://github.com/samu-delucas/dots.git $HOME/.dotsrepo
# 3. Set an alias for this session
# (the same alias is included in ~/.dots/shell/.aliasrc)
alias .git='/usr/bin/git --git-dir=$HOME/.dotsrepo/.git --work-tree=$HOME'
# 4. Don't show untracked files (we only want to track the ones that we add)
.git config --local status.showUntrackedFiles no
# 5. Get the actual files (I think lol)
# If there is an error with existing files, backup the files and try again
.git checkout
if [ $? = 0 ]; then
  echo "Checked out correctly.";
  else
    echo "Backing up pre-existing dot files.";
    mkdir -p .config-backup
    .git checkout 2>&1 | egrep "\s+\." | awk {'print $1'} | xargs -I{} mv {} .config-backup/{}
fi;

### Setting paths
sudo echo "export ZDOTDIR=$HOME/.dots/shell/zsh" >> /etc/zsh/zshenv
