import os
from pathlib import Path

user = os.environ['SUDO_USER'] if 'SUDO_USER' in os.environ else os.environ['USER']
home = str(Path.home())

os.system('apt update && apt upgrade -y')
os.system('apt-get install i3 gnome-terminal ubuntu-drivers-common mesa-utils mesa-utils-extra gnupg xautolock xorg xserver-xorg wget unzip wpasupplicant')

bash_profile = open(f'/home/{user}/.profile', 'a')
xinitrc = open(f'/home/{user}/.xinitrc', 'a')
chunk1 = '# Auto start i3\nif [[ -z $DISPLAY ]] && [[ $(tty) = /dev/tty1 ]]; then\n  startx\nfi'
chunk2 = 'export TERMINAL = "gnome-terminal"\nalias open="xdg-open"\ni3'

bash_profile.write(chunk1)
xinitrc.write(chunk2)

# os.system('reboot now')
