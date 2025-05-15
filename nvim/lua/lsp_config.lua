-- Mason Configuration

require("mason").setup()

-- MasonLsp Configuration

require("mason-lspconfig").setup {
    --
    ensure_installed = { 
        "lua_ls", "texlab", "clangd", "jdtls","bashls","pyright","asm_lsp","hls","solargraph"},
}

-- Servers Configuration


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
    vim.keymap.set('n', '<leader>cf', vim.lsp.buf.format, opts)
end

local lsp = require('lspconfig')
local capabilities = require('cmp_nvim_lsp').default_capabilities()


lsp.clangd.setup{
    on_attach = on_attach,
    capabilities = capabilities
}

lsp.hls.setup{
    on_attach = on_attach,
    capabilities = capabilities
}

lsp.jdtls.setup{
    on_attach = on_attach,
    capabilities = capabilities
}

lsp.pyright.setup{
    on_attach = on_attach,
    capabilities = capabilities
}

lsp.texlab.setup{
    on_attach = on_attach,
    capabilities = capabilities
}

lsp.asm_lsp.setup{
    on_attach = on_attach,
    capabilities = capabilities,
    root_dir = function (fname)
        return vim.fn.getcwd()
    end,
}

lsp.bashls.setup({
    on_attach = on_attach,
    capabilities = capabilities,
    root_dir = function (fname)
        return vim.fn.getcwd()
    end,
    bashIde = {
        globPattern = "*@(.sh|.inc|.bash|.command)"
    }
})

lsp.solargraph.setup({
    on_attach = on_attach,
    capabilities = capabilities
})

lsp.lua_ls.setup{
    on_attach = on_attach,
    capabilities = capabilities,
    on_init = function(client)
        local path = client.workspace_folders[1].name
        if vim.loop.fs_stat(path..'/.luarc.json') or vim.loop.fs_stat(path..'/.luarc.jsonc') then
          return
    end

    client.config.settings.Lua = vim.tbl_deep_extend('force', client.config.settings.Lua, {
        runtime = {
            -- Tell the language server which version of Lua you're using
            -- (most likely LuaJIT in the case of Neovim)
            version = 'LuaJIT'
        },
        -- Make the server aware of Neovim runtime files
        workspace = {
            checkThirdParty = false,
            library = {
                vim.env.VIMRUNTIME
                -- Depending on the usage, you might want to add additional paths here.
                -- "${3rd}/luv/library"
                -- "${3rd}/busted/library",
            }
            -- or pull in all of 'runtimepath'. NOTE: this is a lot slower
            -- library = vim.api.nvim_get_runtime_file("", true)
        }
    })
  end,
  settings = {
    Lua = {}
  }
}
