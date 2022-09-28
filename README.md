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
1) Run Script on server machine
2) Control VPN with 'menu' script
3) Move .ovpn file to client machine
4) Have openvpn installed on client machine
5) Use VPN on client with "$ sudo openvpn zerotrust.ovpn"
```
```
-- PiHole
0) sudo vim /etc/openvpn/server/server.conf
1) echo 'push "dhcp-option DNS 10.8.0.1"' >> /etc/openvpn/server/server.conf
2) sudo systemctl restart openvpn-server@server
3) sudo echo -e '127.0.0.1\t$(hostname)' >> /etc/hosts
```
```
-- UFW
1) ufw allow proto tcp from 10.8.0.0/24 to 10.8.0.1 port 80
2) ufw allow proto tcp from 10.8.0.0/24 to 10.8.0.1 port 53
3) ufw allow proto udp from 10.8.0.0/24 to 10.8.0.1 port 53
```
