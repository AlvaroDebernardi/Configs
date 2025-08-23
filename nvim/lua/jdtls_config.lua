local on_attach = function(_, bufnr)
    -- Mappings.
    local opts = { buffer = bufnr, noremap = true, silent = true }

    vim.bo[bufnr].omnifunc = 'v:lua.vim.lsp.omnifunc'
    vim.keymap.set('n', 'K', vim.lsp.buf.hover, opts)

    vim.keymap.set('n', 'gD', vim.lsp.buf.declaration, opts)
    vim.keymap.set('n', 'gd', vim.lsp.buf.definition, opts)
    vim.keymap.set('n', 'gr', vim.lsp.buf.references, opts)
    vim.keymap.set('n', 'gi', vim.lsp.buf.implementation, opts)

    vim.keymap.set('n', '<leader>td', vim.lsp.buf.type_definition, opts)
    vim.keymap.set('n', '<leader>rn', vim.lsp.buf.rename, opts)

    vim.diagnostic.config({
        float=true,
        virtual_text=false,
        underline={ severity= { min = vim.diagnostic.severity.HINT }},
    })
    vim.keymap.set('n', '<leader>em', vim.diagnostic.open_float, opts)
    vim.keymap.set('n', '<leader>ep', vim.diagnostic.goto_prev, opts)
    vim.keymap.set('n', '<leader>en', vim.diagnostic.goto_next, opts)
    vim.keymap.set('n', '<leader>ca', vim.lsp.buf.code_action, opts)
end

local capabilities = require('cmp_nvim_lsp').default_capabilities()

vim.api.nvim_create_autocmd("FileType", {
  pattern = "java",
  callback = function()
    local jdtls = require("jdtls")

    local root_markers = { "gradlew", "mvnw", ".git", "build.gradle", "pom.xml" }
    local root_dir = require("jdtls.setup").find_root(root_markers)
    local workspace_dir = vim.fn.stdpath("data") .. "/jdtls-workspace/" .. vim.fn.fnamemodify(root_dir, ":p:h:t")

    jdtls.start_or_attach({
      cmd = { "jdtls", "-data", workspace_dir },
      root_dir = root_dir,
      capabilities = capabilities,
      on_attach = on_attach,
    })
  end,
})
