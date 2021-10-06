#
# .dots/wm/qtile/screens.py
#
# Screens config
#

from libqtile import bar
from libqtile.config import Screen
from widgets import widgets

screens = [Screen(wallpaper="~/wallpapers/016.jpg",
                  wallpaper_mode="fill",
                  top=bar.Bar(widgets, size=35, opacity=1.0))]
