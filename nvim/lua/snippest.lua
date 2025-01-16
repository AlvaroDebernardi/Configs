_G.setKeymap = function(stringMap)
    local position = vim.api.nvim_win_get_cursor(0)
    local row,col = position[1], position[2]
    local line = vim.api.nvim_get_current_line()
    local snipp =  line:sub(1,col) .. stringMap .. line:sub(col+1)
    vim.api.nvim_buf_set_lines(0, row - 1, row, false, {snipp})
    vim.api.nvim_win_set_cursor(0,{row,col+string.len(stringMap)-1})
end

vim.api.nvim_create_autocmd("FileType", { pattern = "markdown",

    callback = function()

        vim.api.nvim_buf_set_keymap(0, "n", "<leader>sn", "", {
            noremap = true,
            silent = true,
            callback = function() _G.setKeymap("[!Note]") end,
        })

        vim.api.nvim_buf_set_keymap(0, "n", "<leader>st", "", {
            noremap = true,
            silent = true,
            callback = function () _G.setKeymap("[!Tip]") end
        })

        vim.api.nvim_buf_set_keymap(0, "n", "<leader>sw", "", {
            noremap = true,
            silent = true,
            callback = function() _G.setKeymap("[!Warning]") end,
        })

        vim.api.nvim_buf_set_keymap(0, "n", "<leader>si", "", {
            noremap = true,
            silent = true,
            callback = function() _G.setKeymap("[!Important]") end,
        })

        vim.api.nvim_buf_set_keymap(0, "n", "<leader>se", "", {
            noremap = true,
            silent = true,
            callback = function() _G.setKeymap("[!Error]") end,
        })
    end,
})
