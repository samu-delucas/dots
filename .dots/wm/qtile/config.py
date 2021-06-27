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
widget_defaults = dict(font='sans', fontsize=12, padding=3)  # Default
extension_defaults = widget_defaults.copy()  # Default
reconfigure_screens = True  # Default
auto_minimize = True  # Default

# Unnecesary line but needed for java UI toolkits or sth lol
wmname = 'LG3D'
