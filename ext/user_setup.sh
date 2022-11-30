#!/bin/sh
USERNAME=webmaster
useradd $USERNAME
passwd $USERNAME
usermod -aG wheel $USERNAME
usermod --shell /bin/zsh $USERNAME
su $USERNAME
mkdir /$USERNAME
echo "[*] User information:"
cat /etc/passwd | grep $USERNAME || echo "[x] Error setting user account"
echo "[*] Permissions informations:"
sudo -l -U webserver | grep "ALL" || echo "[x] Error setting user permissions"
