import os

os.system('apt update && apt upgrade -y')
os.system('apt-get install i3 ubuntu-drivers-common mesa-utils mesa-tils-extra gnupg xautolock xorg xserver-xorg wget unzip wpasupplicant')

os.system('apt-get install gnome-terminal -y')
os.system('reboot now')
