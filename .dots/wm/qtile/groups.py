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


# matches=[Match(wm_class=[re.compile('^(?!.*Alacritty).*$')])])
# matches=[Match(wm_class=[re.compile('!firefox|!discord|!Alacritty')])])

groups = [
    # Group('term', label='  ',
    #       matches=[Match(wm_class=['Alacritty'])], position=1),
    Group('1',
          label='',
          matches=[Match(wm_class=['firefox'])]
          ),
    Group('2',
          label=''
          ),
    Group('3',
          label='',
          matches=[Match(wm_class=['discord', 'teams-for-linux', 'Signal'])]
          ),
    Group('4',
          label=''
          ),
    Group('5',
          label='',
          matches=[Match(wm_class=['Spotify'])]
          ),
    Group('6',
          label='',
          matches=[Match(wm_class=['Lutris'])]
          ),
    Group('7',
          label=''
          ),
    Group('8',
          label=''
          ),
    Group('9',
          label=''
          ),
    Group('0',
          label='',
          )
]

for i in groups:
    keys.extend([
        # Switch to group N
        Key([mod], i.name, lazy.group[i.name].toscreen(toggle=False)),

        # Send window to group N
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name))
        # Key([mod, "shift"], current_key, lazy.window.togroup(group.name, switch_group=True))
    ])
