require('render-markdown').setup({
    render_modes = true,
    heading = {
        position = 'overlay',
        width = 'block',
    },
    callout = {
        note = { quote_icon = '│' },
        important = { quote_icon = '│' },
    },
    dash = {
        width = 90,
    }

})
