#!/bin/sh

#
# Notes: if you are behind a NAT, you will also need to do the following:
# IFACE=$(echo $(ip r | grep default) | cut -d " " -f5)
# iptables -t nat -A POSTROUTING  -s 10.8.0.0/24 -o $IFACE -j MASQUERADE
#

sudo iptables -I INPUT -p tcp -m tcp --dport 22 -j ACCEPT
sudo iptables -I INPUT -p tcp -m tcp --dport 80 -j ACCEPT
sudo iptables -I INPUT -p tcp -m tcp --dport 443 -j ACCEPT
sudo iptables -I INPUT -p tcp -m tcp --dport 53 -j ACCEPT
sudo iptables -I INPUT -p tcp -m tcp --dport all -j DENY
