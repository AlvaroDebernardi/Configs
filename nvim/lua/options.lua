--Numbers
vim.opt.relativenumber = true
vim.opt.number = true

--Clipboard
vim.o.clipboard = unnamedplus
vim.keymap.set('v', '<C-c>', '"+y')
vim.keymap.set('n', '<leader><C-v>', '"+p')

--Tabs and Indent
vim.opt.tabstop = 4
vim.opt.softtabstop = 4
vim.opt.shiftwidth = 4
vim.opt.expandtab = true
vim.opt.smartindent = true

vim.opthlsearch = false
vim.opt.incsearch = true

vim.opt.scrolloff = 11

vim.opt.colorcolumn = "80"
vim.opt.linebreack = true

vim.o.foldmethod = "expr"
vim.o.foldexpr = "nvim_treesitter#foldexpr()"
vim.o.foldlevel = 99

--Movements
vim.keymap.set('n', 'E', 'ge', { noremap = true })

--Set Leader
vim.g.mapleader = " "
vim.g.maplocalleader = " "

--Save And Quit
vim.keymap.set('n', '<leader>w', ':w<CR>')
vim.keymap.set('n', '<leader>q', ':q<CR>')

--Project Managemt
vim.keymap.set('n', '<leader>pv', vim.cmd.Ex)
vim.keymap.set('n', '<leader>pn', ':e')

--Buffer Managent
vim.keymap.set('n', '<leader>bv', ':buffers<CR>', {noremap = true})
vim.keymap.set('n', '<leader>bp', ':bp<CR>', {noremap = true})
vim.keymap.set('n', '<leader>bn', ':bn<CR>', {noremap = true})
vim.keymap.set('n', '<leader>bd', ':bd<CR>', {noremap = true})

--Tabs Managent
vim.keymap.set('n', '<leader>tv', ':tabs<CR>', {noremap = true})
vim.keymap.set('n', '<leader>tn', ':tabnew<CR>', {noremap = true})
vim.keymap.set('n', '<leader>tq', ':tabclose<CR>', {noremap = true})
vim.keymap.set('n', '<leader>tp', ':tabp<CR>', {noremap = true})
vim.keymap.set('n', '<leader>tn', ':tabn<CR>', {noremap = true})

--Windows Managemt
vim.keymap.set('n', '<leader>sh', vim.cmd.split)
vim.keymap.set('n', '<leader>sv', vim.cmd.vsplit)

vim.keymap.set('n', '<leader>h', '<C-w>h')
vim.keymap.set('n', '<leader>j', '<C-w>j')
vim.keymap.set('n', '<leader>k', '<C-w>k')
vim.keymap.set('n', '<leader>l', '<C-w>l')

vim.keymap.set('n', '<leader>H', '<C-w>H')
vim.keymap.set('n', '<leader>J', '<C-w>J')
vim.keymap.set('n', '<leader>K', '<C-w>K')
vim.keymap.set('n', '<leader>L', '<C-w>L')

vim.keymap.set('n', '<leader>+', '2<C-w>+')
vim.keymap.set('n', '<leader>-', '2<C-w>-')
vim.keymap.set('n', '<leader>>', '3<C-w>>')
vim.keymap.set('n', '<leader><', '3<C-w><')

--Terminal Mode Managemt
vim.keymap.set('n', '<leader><CR>', ':vsplit<CR><C-w>l:term<CR>18<C-w><i')

vim.keymap.set('t', '<C-h>', '<C-\\><C-n><C-w>h')
vim.keymap.set('t', '<C-j>', '<C-\\><C-n><C-w>j')
vim.keymap.set('t', '<C-k>', '<C-\\><C-n><C-w>k')
vim.keymap.set('t', '<C-l>', '<C-\\><C-n><C-w>l')

--Insert Mode Management
vim.keymap.set('i', '<C-a>', '<C-c>zza')

--Normal Mode Managemetn
vim.keymap.set('n', 'm', 'o<C-c>k')
vim.keymap.set('n', 'M', 'O<C-c>j')
