from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from datetime import datetime
import subprocess

mod = "mod4"
alt = "mod1"
altGr = "mod3"
terminal = "kitty"

@hook.subscribe.startup
def set_basic_configuration():
    subprocess.run(['setxkbmap', 'latam'])
    subprocess.run(['sct','2700'])
    subprocess.run(['picom','--daemon'])

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

# Focus Windows Movements
    Key([alt], "h", lazy.layout.left(), 
        desc="Move focus to left"),

    Key([alt], "l", lazy.layout.right(), 
        desc="Move focus to right"),

    Key([alt], "j", lazy.layout.down(), 
        desc="Move focus down"),

    Key([alt], "k", lazy.layout.up(), 
        desc="Move focus up"),

# Windows Movements
    Key([mod], "space", lazy.layout.next(), 
        desc="Move window focus to other window"),

    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), 
        desc="Move window to the left"),

    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), 
        desc="Move window to the right"),

    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), 
        desc="Move window down"),

    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), 
        desc="Move window up"),

# Size Windows Managent
    Key([mod, "control"], "h", lazy.layout.grow_left(), 
        desc="Grow window to the left"),

    Key([mod, "control"], "l", lazy.layout.grow_right(), 
        desc="Grow window to the right"),

    Key([mod, "control"], "j", lazy.layout.grow_down(), 
        desc="Grow window down"),

    Key([mod, "control"], "k", lazy.layout.grow_up(), 
        desc="Grow window up"),

    Key([mod], "n", lazy.layout.normalize(), 
        desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",),

# Launching Applications
    Key([mod], "Return", lazy.spawn(terminal), 
        desc="Launch terminal"),

    Key([mod], "d", lazy.spawn("discord"), 
        desc="Launch discord"),

    Key([mod], "b", lazy.spawn("brave"), 
        desc="Launch brave"),

    Key([], "print", lazy.spawn("flameshot gui"), 
        desc="Take Screenshot"),

# Layout Managent
    Key([mod], "Tab", lazy.next_layout(), 
        desc="Toggle between layouts"),

    Key( [mod], "f", lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",),

    Key([mod], "t", lazy.window.toggle_floating(), 
        desc="Toggle floating on the focused window"),

    Key([mod], "w", lazy.window.kill(), 
        desc="Kill focused window"),

# Qtile Managent
    Key([mod, "control"], "q", lazy.shutdown(), 
        desc="Shutdown Qtile"),

    Key([mod], "r", lazy.spawncmd(), 
        desc="Spawn a command using a prompt widget"),

    Key([mod, "control"], "r", lazy.reload_config(), 
        desc="Reload the config"),
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as 
# it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using 
# .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


#groups = [Group(i) for i in "123456789"]
groups = []

groups_names = ["1","2","3","4","0"]
groups_labels = [" "," ","󰜈 ","󰙯 ",""]
groups_layouts = ["max","monadtall","max","max","max"]

for i in range(len(groups_names)):
    groups.append(
            Group(
                name=groups_names[i],
                label=groups_labels[i],
                layout=groups_layouts[i],))

for i in groups:
    keys.extend(
        [
            Key([mod], i.name, lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),),

            Key([mod, "shift"], i.name, 
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),),
        ]
    )

layouts = [
    layout.Max(),
    layout.MonadTall(border_width=0, margin=3, ratio=.65),
    # layout.Columns(border_width=0, margin=1), # layout.MonadWide(),
    # layout.Stack(num_stacks=2), layout.Bsp(), layout.Matrix(), layout.RatioTile(),
    # layout.Tile(), layout.TreeTab(), layout.VerticalTile(), layout.Zoomy(),
]

widget_defaults = dict(
    font="HackNerdFont",
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

day_of_year = datetime.today().timetuple().tm_yday
perc_of_year = (day_of_year/365)*100

screens = [
    Screen(
        wallpaper = '~/.config/qtile/Wallpapers/samuray.jpg', 
        wallpaper_mode='fill',
        top=bar.Bar(
            [
                widget.TextBox(text = " 󰣇",fontsize = 18,
                               foreground='#1793d1'),
                widget.TextBox(text = "  ",fontsize = 18,
                               foreground='d7a65f'),
                widget.Sep(linewidth=1,padding=15,foreground='a485dd',size_percent=70),
                widget.GroupBox(highlight_method='line',
                                highlight_color=['11121d','215578'],
                                inactive = '3a6b76',
                                active = '99aa40',
                                fontsize=18,
                                this_current_screen_border='215578',),
                widget.Sep(linewidth=1,foreground='a485dd',
                           padding=15, size_percent=70),
                widget.CurrentLayoutIcon(padding=5,scale=0.58),
                widget.Prompt(),
                widget.Spacer(),
                widget.Sep(linewidth=1,padding=15,foreground='a485dd',size_percent=70),
                widget.Clock(format="%H:%M", fontsize=16),
                widget.Sep(linewidth=1,padding=15,foreground='a485dd',size_percent=70),
                widget.Spacer(),

                widget.Sep(linewidth=1,foreground='a485dd',size_percent=70),

                #HardWare Information
                widget.CPU(format='{load_percent}%  ',
                           foreground='ee6d85',
                           padding=10),
                widget.ThermalSensor(format='{temp:.1f} 󰔄',
                                     threshold=75,
                                     foreground='95c561',
                                     padding=10),
                widget.Memory(format='{MemUsed:.2f}Gb  ',
                              measure_mem='G',
                              foreground='d7a65f',
                              padding=10),
                widget.DF(visible_on_warn=False,
                          format='{f}Gb  ',
                          foreground='7199ee',
                          padding=10),
                widget.Battery(format='{percent:2.0%} 󰂏 '),
                widget.Net(format="{down:.1f} {down_suffix}",
                           prefix="M"),
                widget.Sep(linewidth=1,foreground='a485dd',size_percent=70),
                widget.Clock(format=" %-d/%-m/%y"),
                widget.WidgetBox(
                    widgets=[
                        widget.TextBox(text = f"{perc_of_year:.2f}"+'%',fontsize = 14, foreground='d7a65f'),
                    ],
                    fontsize=16,
                    text_closed=" ",
                    text_open=" ",
                    close_button_location='right',
                ),
                widget.Sep(linewidth=1,foreground='a485dd',size_percent=70),
                widget.QuickExit(fontsize=18,default_text='   ',foreground='a485dd'),
            ],
            30,
            margin=[3,3,2,3],
            background = '11121da5',
            #border_width=1,
            #border_color='a485dd',
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
    Screen(
        wallpaper = '~/.config/qtile/Wallpapers/samuray.jpg', 
        wallpaper_mode='fill',
        top=bar.Bar(
            [
                widget.TextBox(text = " 󰣇",fontsize = 18,
                               foreground='#1793d1'),
                widget.TextBox(text = "  ",fontsize = 18,
                               foreground='d7a65f'),
                widget.Sep(linewidth=1,padding=15,foreground='a485dd',size_percent=70),
                widget.GroupBox(highlight_method='line',
                                highlight_color=['11121d','215578'],
                                inactive = '3a6b76',
                                active = '99aa40',
                                fontsize=18,
                                this_current_screen_border='215578',),
                widget.Sep(linewidth=1,foreground='a485dd',
                           padding=15, size_percent=70),
                widget.CurrentLayoutIcon(padding=5,scale=0.58),
                widget.Prompt(),
                widget.Spacer(),
                widget.Sep(linewidth=1,padding=15,foreground='a485dd',size_percent=70),
                widget.Clock(format="%H:%M", fontsize=16),
                widget.Sep(linewidth=1,padding=15,foreground='a485dd',size_percent=70),
                widget.Spacer(),

                widget.Sep(linewidth=1,foreground='a485dd',size_percent=70),

                #HardWare Information
                widget.CPU(format='{load_percent}%  ',
                           foreground='ee6d85',
                           padding=10),
                widget.ThermalSensor(format='{temp:.1f} 󰔄',
                                     threshold=75,
                                     foreground='95c561',
                                     padding=10),
                widget.Memory(format='{MemUsed:.1f}Gb  ',
                              measure_mem='G',
                              foreground='d7a65f',
                              padding=10),
                widget.DF(visible_on_warn=False,
                          format='{f}Gb  ',
                          foreground='7199ee',
                          padding=10),
                #widget.Battery(format='{percent:2.0%} 󰂏 '),
                widget.Net(format="{down:.1f} {down_suffix}",
                           prefix="M"),
                widget.Sep(linewidth=1,foreground='a485dd',size_percent=70),
                widget.Clock(format=" %-d/%-m/%y"),
                widget.TextBox(text=" ",fontsize=16),
                widget.Sep(linewidth=1,foreground='a485dd',size_percent=70),
                widget.QuickExit(fontsize=18,default_text='   ',foreground='a485dd'),
            ],
            30,
            margin=[3,3,2,3],
            background = '11121da5',
            #border_width=1,
            #border_color='a485dd',
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Scratchpads

trans = "kitty trans "\
            "-show-dictionary n "\
            "-show-original n "\
            "-show-translation n "\
            "-show-languages n "\
            "-show-prompt-message n "\
            "-show-alternatives Y "

groups.append(ScratchPad('scratchpad',[
    DropDown('term','kitty', width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.98),
    DropDown('translateEs','kitty trans -b :es' ,width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.98),
    DropDown('translateEn',trans + ':en' ,width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.98)
]))


keys.extend([
    Key([alt], "Return", lazy.group['scratchpad'].dropdown_toggle('term')),
    Key([alt], "e", lazy.group['scratchpad'].dropdown_toggle('translateEs')),
    Key([alt], "i", lazy.group['scratchpad'].dropdown_toggle('translateEn'))
])


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry

        Match(title="Cosmetic"),
        Match(wm_class="feh"),  # For Images
        Match(title="Tomi"),
    ],
    border_focus='a485dd',
    border_width=1,
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
