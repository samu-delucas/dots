" auto-install vim-plug
if empty(glob('~/.config/nvim/autoload/plug.vim'))
  silent !curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  "autocmd VimEnter * PlugInstall
  "autocmd VimEnter * PlugInstall | source $MYVIMRC
endif

call plug#begin('~/.config/nvim/autoload/plugged')

    " Startify (start fancy menu)
    " Plug 'mhinz/vim-startify', {'branch': 'center'}
    " Better Syntax Support
    Plug 'sheerun/vim-polyglot'
    " Auto pairs for '(' '[' '{'
    Plug 'jiangmiao/auto-pairs'
    " Bottom status line
    Plug 'itchyny/lightline.vim'
    " CoC
    Plug 'neoclide/coc.nvim', {'branch': 'release'}
    " Comment a line easily
    Plug 'tpope/vim-commentary'
    " Snippets
    Plug 'honza/vim-snippets'
    " Which key
    " Plug 'liuchengxu/vim-which-key'   
    

    " Themes
    Plug 'ayu-theme/ayu-vim'
    Plug 'morhetz/gruvbox'

    " Git
    Plug 'mhinz/vim-signify'        " show changes with +,-,etc

call plug#end()
