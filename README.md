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
