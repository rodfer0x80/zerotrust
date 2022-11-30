#!/bin/sh

ufw allow proto tcp from 0.0.0.0/0 port 80
ufw allow proto tcp from 0.0.0.0/0 port 53
ufw allow proto udp from 0.0.0.0/0 port 53
