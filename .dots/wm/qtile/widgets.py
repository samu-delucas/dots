# Imports

from libqtile import widget, bar
from colors import colors
import os

widgetFont = "Hack Nerd Font Mono"

def sep(pd=10, bg=0):
    return widget.Sep(
        background=colors[bg],
        padding=pd,
        linewidth=0,
    )

def leftsep(fg):
    return widget.TextBox(
        text="\ue0b6",
        fonts="Hack Nerd Font Mono",    # It is not widgetFont because it needs to be a nerdfont
        foreground=colors[fg],
        background=colors[0],
        padding=0,
        fontsize=38
    )

def rightsep(fg):
    return widget.TextBox(
        text="\ue0b4",
        fonts="Hack Nerd Font Mono",    # It is not widgetFont because it needs to be a nerdfont
        foreground=colors[fg],
        background=colors[0],
        padding=0,
        fontsize=38
    )


def parse_win_name(txt):
    '''Parse window titles so "Mozilla Firefox" appears first'''

    if " — Mozilla Firefox" in txt:
        txt = txt.replace(" — Mozilla Firefox", "")
        return "Mozilla Firefox — " + txt
    elif " | Microsoft Teams" in txt:
        txt = txt.replace(" | Microsoft Teams", "")
        return "Microsoft Teams — " + txt
    elif " - Lightcord" in txt:
        return "Discord"
    elif " - Filezilla" in txt:
        txt = txt.replace(" - Filezilla", "")
        return "Filezilla —" + txt
    return txt


# Widget default options
widget_defaults = {
    'font': widgetFont,
    'fontsize': 13,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()

# Widgets

widgets = [
    leftsep(4),
    widget.Clock(
        font=widgetFont,
        fontsize=16,
        foreground=colors[5],
        background=colors[4],
        format='%d %b | %A'
    ),
    rightsep(4),

    sep(),

    # leftsep(7),
    # widget.TextBox(
    #     text="",
    #     foreground=colors[5],
    #     background=colors[7],
    #     padding=0,
    #     fontsize=33
    # ),
    # widget.Memory(
    #     background=colors[7],
    #     foreground=colors[5],
    #     font=widgetFont,
    #     fontsize=16,
    #     measure_mem='G',
    #     format='{MemUsed: .2f} GB',
    # ),
    # rightsep(7),

    # sep(),

    leftsep(4),
    widget.CurrentLayoutIcon(
        custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
        scale=0.45,
        padding=0,
        background=colors[4],
    ),
    widget.CurrentLayout(
        background=colors[4],
        foreground=colors[5],
        font=widgetFont,
        fontsize=15,
    ),
    rightsep(4),

    sep(),

    widget.Prompt(
        foreground=colors[4],
        cursor=False,
        # cursor_color=colors[4],   #Da problemas
        font=widgetFont,
        prompt='> ',
    ),

    widget.Spacer(),

    widget.GroupBox(
        font=widgetFont,
        fontsize=14,
        active=colors[4],
        inactive=colors[1],
        rounded=True,
        highlight_color=colors[0],
        highlight_method="line",
        this_current_screen_border=colors[0],
        block_highlight_text_color=colors[5],
        blockwidth=2,
        margin_y=5,
    ),

    widget.Spacer(),

    sep(),

    leftsep(4),
    widget.Volume(
        background=colors[4],
        foreground=colors[5],
        font=widgetFont,
        fontsize=16,
        # mouse_callbacks={'Button3': lambda: qtile.cmd_spawn("pavucontrol")},
        # update_interval=0.001,
    ),
    rightsep(4),

    sep(),

    # leftsep(3),
    # widget.TextBox(
    #     text="",
    #     foreground=colors[5],
    #     background=colors[3],
    #     padding=0,
    #     fontsize=38
    # ),
    # widget.CPU(
    #     background=colors[3],
    #     foreground=colors[5],
    #     format=' {load_percent}%',
    #     font=widgetFont,
    #     fontsize=16
    # ),
    # sep(6,3),
    # rightsep(3),

    # sep(),

    leftsep(4),
    sep(3,4),
    widget.Battery(
        foreground=colors[5],
        background=colors[4],
        fontsize=24,
        low_percentage=0.2,
        low_foreground=colors[5],
        font="lekton nerd font",
        update_interval=1,
        format='{char}',
        charge_char='ﮣ',
        discharge_char=' ',
    ),
    sep(2,4),
    widget.Battery(
        background=colors[4],
        foreground=colors[5],
        charge_char='↑',
        discharge_char='↓',
        font=widgetFont,
        fontsize=16,
        update_interval=1,
        format='{percent:2.0%}'
    ),
    rightsep(4),

    sep(),

    leftsep(4),
    sep(6,4),
    widget.Clock(
        background=colors[4],
        foreground=colors[5],
        font=widgetFont,
        fontsize=16,
        format='%I:%M %p',
    ),
    rightsep(4),
]
