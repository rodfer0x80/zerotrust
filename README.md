# zerotrust
### Trust nobody? Make your own VPN.
```
--  sshuttle
1) Install ssh and sshuttle on client machine
2) Install ssh and sshd on server machine 
3) Run: $ sshuttle -r <USERNAME>@<IP_ADDRESS> 0.0.0.0/0 --dns
```
```
--  OpenVPN
1) Read script before installing or atleast run a checksum check
1) sudo ./openvpn_install
2) Control VPN with 'menu' script
3) Move .ovpn file to client machine
4) Have openvpn installed on client machine
5) Use VPN on client with "$ sudo openvpn zerotrust.ovpn"
```
```
-- PiHole / PiVPN
1) sudo vim /etc/pihole/setupVars.conf [IPV4_ADDRESS=10.8.0.1/24]
2) sudo vim /etc/openvpn/server/server.conf [push "dhcp-option DNS 10.8.0.1"]
3) sudo systemctl restart openvpn-server@server
4) sudo echo -e '127.0.0.1\t$(hostname)' >> /etc/hosts
```
```
-- UFW
1) ufw allow proto tcp from 10.8.0.0/24 to 10.8.0.1 port 80
2) ufw allow proto tcp from 10.8.0.0/24 to 10.8.0.1 port 53
3) ufw allow proto udp from 10.8.0.0/24 to 10.8.0.1 port 53
```

## Research
- Setup pivpn (pihole+openvpn) [https://www.scaleway.com/en/docs/tutorials/pihole-vpn/]
- Setup OpenVPN with PiHole on AWS [https://victoria.dev/blog/set-up-a-pi-hole-vpn-on-an-aws-lightsail-instance/]
