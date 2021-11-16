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
    Plug 'vim-airline/vim-airline'
    " CoC
    Plug 'neoclide/coc.nvim', {'branch': 'release'}
    " Comment a line easily
    Plug 'tpope/vim-commentary'
    " Snippets
    Plug 'honza/vim-snippets'
    Plug 'sirver/ultisnips'
    let g:UltiSnipsExpandTrigger = '<tab>'
    let g:UltiSnipsJumpForwardTrigger = '<tab>'
    let g:UltiSnipsJumpBackwardTrigger = '<s-tab>'
    " Which key
    Plug 'liuchengxu/vim-which-key'   
    
    " Tabs/bufferline
    Plug 'kyazdani42/nvim-web-devicons' " Recommended (for coloured icons)
    " Plug 'ryanoasis/vim-devicons' Icons without colours
    Plug 'akinsho/bufferline.nvim'

    " Themes
    " Plug 'ayu-theme/ayu-vim'
    " Plug 'morhetz/gruvbox'
    " Plug 'joshdick/onedark.vim'
    Plug 'embark-theme/vim', {'as': 'embark'}

    " Git
    Plug 'mhinz/vim-signify'        " show changes with +,-,etc

    " Plugin para R 
    " Plug 'jalvesaq/Nvim-R', {'branch': 'stable'}
    " Plugin para LaTex
    Plug 'lervag/vimtex'

call plug#end()
