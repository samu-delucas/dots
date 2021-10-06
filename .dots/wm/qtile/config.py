#
# .dots/wm/qtile/config.py
#
# Set up general settings and import all the config files
# See: https://docs.qtile.org/en/latest/manual/config/index.html
#

# Imports
from keys import mod, keys
from layouts import layouts
from mouse import mouse
from groups import groups
from screens import screens

# General settings
auto_fullscreen = True
bring_front_click = False
cursor_warp = False
dgroups_key_binder = None   # Maybe change it in the future?
dgroups_app_groups = []     # Useful! TODO: change it!
# TODO: floating layout (separate file)
focus_on_window_activation = "smart"
follow_mouse_focus = False
reconfigure_screens = True  # Default
auto_minimize = True  # Default

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = 'qtile'
