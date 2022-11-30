#!/bin/sh

# Set default chain policies
sudo iptables -P INPUT DROP
sudo iptables -P FORWARD DROP
sudo iptables -P OUTPUT ACCEPT
# SSH
sudo iptables -I INPUT -p tcp -m tcp --dport 22 -j ACCEPT
# HTTP
sudo iptables -I INPUT -p tcp -m tcp --dport 80 -j ACCEPT
sudo iptables -I INPUT -p udp -m udp --dport 80 -j ACCEPT
# OpenVPN
sudo iptables -I INPUT -p tcp -m tcp --dport 1194 -j ACCEPT
sudo iptables -I INPUT -p udp -m udp --dport 1194 -j ACCEPT
# DNS
sudo iptables -I INPUT -p tcp -m tcp --dport 53 -j ACCEPT
sudo iptables -I INPUT -p udp -m udp --dport 53 -j ACCEPT
# Accept on localhost
sudo iptables -A INPUT -i lo -j ACCEPT
sudo iptables -A OUTPUT -o lo -j ACCEPT
# Notes: if you are behind a NAT, you will also need to do the following:
IFACE=$(echo $(ip r | grep default) | cut -d " " -f5)
echo $IFACE
sudo iptables -t nat -A POSTROUTING  -s 10.8.0.0/24 -o $IFACE -j MASQUERADE
# Allow established sessions to receive traffic
sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

