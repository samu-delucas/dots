#
# .dots/wm/qtile/groups.py
#
# Groups (workspaces) configuration
#

from libqtile.command import lazy
from libqtile.config import Key, Group, Match
from keys import mod, keys
import re

# Run this command to find the WM_CLASS of a window:
#   xprop | grep WM_CLASS | awk '{print $4}'
#
# For more icons see https://www.nerdfonts.com/cheat-sheet
groups = [
    # Group('term', label='  ',
    #       matches=[Match(wm_class=['Alacritty'])], position=1),
    Group('term',    label='', position=1),
    Group('browser', label='', position=2,
          matches=[Match(wm_class=['firefox'])]),
    Group('discord', label='ﭮ', position=3,
          matches=[Match(wm_class=['lightcord'])]),
    Group('misc',    label='', position=4)
    # matches=[Match(wm_class=[re.compile('^(?!.*Alacritty).*$')])])
    # matches=[Match(wm_class=[re.compile('!firefox|!discord|!Alacritty')])])
]

for i, group in enumerate(groups):
    current_key = str(i + 1)
    keys.extend([
        # Switch to group N
        Key([mod], current_key, lazy.group[group.name].toscreen(toggle=False)),

        # Send window to group N
        Key([mod, "shift"], current_key, lazy.window.togroup(group.name))
        # Key([mod, "shift"], current_key, lazy.window.togroup(group.name, switch_group=True))
    ])
