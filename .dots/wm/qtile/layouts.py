#
# .dots/wm/qtile/layouts.py
#
# Layouts
#

from libqtile import layout

layouts = [
    layout.Columns(
        margin=10,
        margin_on_single=10,
        border_focus='#FBFBFB',
        border_focus_stack='#F9D002',
        border_normal='#111111',
        border_normal_stack='#111111',
        border_on_single=False,
        border_width=3,
        fair=False,
        insert_position=1
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]
