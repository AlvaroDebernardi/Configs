vim.api.nvim_create_autocmd("FileType", {
  pattern = { "tex", "plaintex", "latex" },
  callback = function()
    vim.opt_local.tabstop = 2
    vim.opt_local.shiftwidth = 2
    vim.opt_local.softtabstop = 2
    vim.opt_local.expandtab = true
    vim.api.nvim_set_keymap("n", "<leader>c", ":!tectonic %<CR>", { noremap = true, silent = true })
  end,
})

