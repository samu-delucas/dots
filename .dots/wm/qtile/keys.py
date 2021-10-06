#
# .dots/wm/qtile/keys.py
#
# Key Bindings
#

from libqtile.command import lazy
from libqtile.config import Key, Group

mod = "mod4"    # Meta

keys = [Key(t[0], t[1], *t[2:]) for t in [

    # Main bindings
    ([mod], "w",        lazy.window.kill()),
    ([mod], "r",        lazy.spawncmd()),

    # Qtile managment
    ([mod, "control"], "r", lazy.restart()),
    ([mod, "control"], "q", lazy.shutdown()),

    # Spawn applications

    ([mod], "Return",   lazy.spawn("alacritty")),
    ([mod], "b",   lazy.spawn("firefox")),
    ([mod], "d",   lazy.spawn("lightcord")),
    ([mod], "f",   lazy.spawn("thunar")),
    ([mod], "g",   lazy.spawn("lutris")),
    ([mod], "m",   lazy.spawn("freezer")),
    ([mod], "z",   lazy.spawn("zathura")),

    # Switch between layouts
    ([mod],          "Tab",    lazy.next_layout()),
    ([mod, "shift"], "Tab",    lazy.prev_layout()),
    ([mod, "shift"], "Return", lazy.layout.toggle_split()),

    # Switch between windows
    ([mod], "h",     lazy.layout.left()),
    ([mod], "l",     lazy.layout.right()),
    ([mod], "j",     lazy.layout.down()),
    ([mod], "k",     lazy.layout.up()),
    ([mod], "space", lazy.layout.next()),

    # Move windows
    ([mod, "shift"], "h", lazy.layout.shuffle_left()),
    ([mod, "shift"], "l", lazy.layout.shuffle_right()),
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Grow windows
    ([mod, "control"], "h", lazy.layout.grow_left()),
    ([mod, "control"], "l", lazy.layout.grow_right()),
    ([mod, "control"], "j", lazy.layout.grow_down()),
    ([mod, "control"], "k", lazy.layout.grow_up()),
    ([mod, "control"], "n", lazy.layout.normalize()),

    # Sound keys
    ([], "XF86AudioMute",         lazy.spawn("amixer -q set Master toggle")),
    ([], "XF86AudioLowerVolume",  lazy.spawn("amixer -c 0 sset Master 1- unmute")),
    ([], "XF86AudioRaiseVolume",  lazy.spawn("amixer -c 0 sset Master 1+ unmute")),

    # Brightness keys
    ([], "XF86MonBrightnessUp",   lazy.spawn("xbacklight -inc 10 -time 100")),
    ([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 10 -time 100")),

]]
