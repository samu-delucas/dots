#
# .dots/wm/qtile/screens.py
#
# Screens config
#

from libqtile import bar
from libqtile.config import Screen
from widgets import widgets
from colors import colors

screens = [
    Screen(
        wallpaper="~/wallpapers/019.jpg",
        wallpaper_mode="fill",
        top=bar.Bar(
            widgets,    # in widgets.py
            size=35,
            background=colors[0],
            border_color=colors[0],
            border_width=colors[0],
            margin=[10, 10, 0, 10],
        )
    )
]
