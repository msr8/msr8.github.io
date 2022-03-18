set number
augroup RestoreCursorShapeOnExit
    autocmd!
    autocmd VimLeave * set guicursor=v-c-sm:block,n-i-ci-ve:ver25,r-cr-o:hor20
augroup END
