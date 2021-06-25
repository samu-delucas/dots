let g:mapleader = "\<Space>"		" set leader key

syntax enable                           " Enables syntax highlighing
set hidden                              " Required to keep multiple buffers open 
set nowrap                              " Display long lines as just one line
set encoding=utf-8                      " The encoding displayed
set fileencoding=utf-8                  " The encoding written to file
set pumheight=10                        " Makes popup menu smaller
set ruler              		            	" Show the cursor position all the time
set cmdheight=2                         " More space for displaying messages
set iskeyword+=-                      	" treat dash separated words as a word text object"
set mouse=a                             " Enable your mouse
set splitbelow                          " Horizontal splits will automatically be below
set splitright                          " Vertical splits will automatically be to the right
set t_Co=256                            " Support 256 colors
set conceallevel=0                      " So that I can see `` in markdown files
set tabstop=2                           " Insert 2 spaces for a tab
set shiftwidth=2                        " Change the number of space characters inserted for indentation
set smarttab                            " Makes tabbing smarter will realize you have 2 vs 4
set expandtab                           " Converts tabs to spaces
set smartindent                         " Makes indenting smart
set autoindent                          " Good auto indent
set laststatus=0                        " Always display the status line
set number                            	" Line numbers
set relativenumber											" The line in which the cursor is will be line number 0
" set cursorline                          " Enable highlighting of the current line
set nohlsearch                          " search doesn't remain highlighted after done searching
set incsearch                           " search incrementally as you type
set scrolloff=8                         " start scrolling when you are 8 lines away from the top/bottom
set noerrorbells                        " annoying beeps/flashes with error msgs
set background=dark                     " tell vim what the background color looks like
set showtabline=2                       " Always show tabs
set noshowmode                          " We don't need to see things like -- INSERT -- anymore
set nobackup                            " This is recommended by coc
set nowritebackup                       " This is recommended by coc
set updatetime=300                      " Faster completion
set timeoutlen=500                      " By default timeoutlen is 1000 ms
set formatoptions-=cro                  " Stop newline continution of comments
set clipboard=unnamedplus               " Copy paste between vim and everything else
" set autochdir                           " Your working directory will always be the same as your working directory
set exrc																" auto source .vimrc if found on the working directory
set signcolumn=yes                      " extra column on the left
" set colorcolumn=80                      " color column at 80 columns (reminds you to keep your code short) I don't like it

au! BufWritePost $MYVIMRC source %      " auto source when writing to init.vm alternatively you can run :source $MYVIMRC

" when running :w!! the file will be saved even if you opened it w/o sudo (little trick) 
cmap w!! w !sudo tee %
