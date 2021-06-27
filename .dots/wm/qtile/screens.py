#
# .dots/wm/qtile/screens.py
#
# Screens config
#

from libqtile import bar
from libqtile.config import Screen
from widgets import widgets

screens = [Screen(top=bar.Bar(widgets, 20, opacity=0.95))]
