#
# .dots/wm/qtile/groups.py
#
# Groups (workspaces) configuration
#

from libqtile.command import lazy
from libqtile.config import Key, Group, Match
from keys import mod, keys

# Run this command to find the WM_CLASS of a window:
#   xprop | grep WM_CLASS | awk '{print $4}'
#
# For more icons see https://www.nerdfonts.com/cheat-sheet
groups = [
    Group('term', label='  ', init=True, persist=True,
          matches=[Match(wm_class=['Alacritty'])], position=1),
    Group('browser', label='  ', init=True, persist=True,
          matches=[Match(wm_class=['firefox'])], position=2),
    Group('discord', label=' ﭮ ', init=True, persist=True,
          matches=[Match(wm_class=['discord'])], position=3),
    Group('misc', label='  ')
]

for i, group in enumerate(groups):
    current_key = str(i + 1)
    keys.extend([
        # Switch to group N. Here toggle=False prevents the group from being toggle
        # with the last used it's already on the screen
        Key([mod], current_key, lazy.group[group.name].toscreen(toggle=False)),

        # Send window to group N
        Key([mod, "shift"], current_key, lazy.window.togroup(group.name))
        # Key([mod, "shift"], current_key, lazy.window.togroup(group.name, switch_group=True))
    ])
