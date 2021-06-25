" Better nav for omnicomplete
" I DONT KNOW
" inoremap <expr> <c-j> ("\<C-n>")
" inoremap <expr> <c-k> ("\<C-p>")

" Use alt + hjkl to resize windows
" I DONT KNOW
" nnoremap <M-j>    :resize -2<CR>
" nnoremap <M-k>    :resize +2<CR>
" nnoremap <M-h>    :vertical resize -2<CR>
" nnoremap <M-l>    :vertical resize +2<CR>

" Easy CAPS
" I DONT KNOW
" inoremap <c-u> <ESC>viwUi
" nnoremap <c-u> viwU<Esc>

" I DONT KNOW
" TAB in general mode will move to text buffer
" nnoremap <TAB> :bnext<CR>
" SHIFT-TAB will go back
" nnoremap <S-TAB> :bprevious<CR>

" Alternate way to save
nnoremap <C-s> :w<CR>
" Alternate way to quit
nnoremap <C-Q> :wq!<CR>
" Use control-c instead of escape
nnoremap <C-c> <Esc>
" <TAB>: completion.
inoremap <expr><TAB> pumvisible() ? "\<C-n>" : "\<TAB>"

" Better tabbing
" I DONT KNOW
" vnoremap < <gv
" vnoremap > >gv

" Better window navigation
" I DONT KNOW
" nnoremap <C-h> <C-w>h
" nnoremap <C-j> <C-w>j
" nnoremap <C-k> <C-w>k
" nnoremap <C-l> <C-w>l

" I DONT KNOW
" nnoremap <Leader>o o<Esc>^Da
" nnoremap <Leader>O O<Esc>^Da

" Comment a line easily
nnoremap <space>/ :Commentary<CR>
vnoremap <space>/ :Commentary<CR>
