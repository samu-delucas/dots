#
# $ZDOTDIR/.zprofile;
# 
# Used for executing USER comands at start, and only
# when starting as a LOGIN shell
#
# Typically used to autostart grafical 
# sessions or set session-wide env variables
#

# Autostart X at login
# more info at https://wiki.archlinux.org/title/Xinit#Autostart_X_at_login
if [ -z "${DISPLAY}" ] && [ "${XDG_VTNR}" -eq 1 ] && [ "$(tty)" = "/dev/tty1" ]; then
  exec startx $XINITRC
fi
