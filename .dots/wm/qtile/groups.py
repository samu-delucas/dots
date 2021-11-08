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
    Group('browser', label='WWW', position=1,
          matches=[Match(wm_class=['firefox'])]),
    Group('term',    label='DEV', position=2),
    Group('chat', label='CHAT', position=3, matches=[
          Match(wm_class=['lightcord', 'teams-for-linux', 'Signal'])]),
    Group('misc',    label='MISC', position=4),
    Group('music', label='MUSIC', position=5,
          matches=[Match(wm_class=['Spotify'])]),
    Group('games', label='GAMES', position=6,
          matches=[Match(wm_class=['Lutris'])])
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
