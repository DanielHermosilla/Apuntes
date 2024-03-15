
let mapleader = "\<Space>"
let maplocalleader = "\<Space>"

" Normal --
noremap <A-j> :m .+1<CR>==
noremap <A-k> :m .-2<CR>==

noremap <tab> >>
noremap <s-tab> <<

noremap <leader>rp :%s/\<C-r><C-w>\>//<CR>
noremap <leader>rn :let @/=expand('<cword>')<cr>cgn

" Insert --
imap jk <Esc>
imap kj <Esc>

imap <S-Right> <Esc>vw
imap <S-Left> <Esc>vb

" Visual --
vnoremap <tab> >gv
vnoremap <s-tab> <gv

vnoremap <A-j> :m '>+1<CR>gv=gv
vnoremap <A-k> :m '<-2<CR>gv=gv

vnoremap p "_dP
vnoremap i <esc>i

" Visual Block --
xnoremap J :m '>+1<CR>gv=gv
xnoremap K :m '<-2<CR>gv=gv
xnoremap <A-j> :m '>+1<CR>gv=gv
xnoremap <A-k> :m '<-2<CR>gv=gv
