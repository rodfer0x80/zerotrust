# zerotrust
### Trust nobody? Make your own VPN.
```
--  sshuttle
1) Install ssh and sshuttle on client machine
2) Install ssh and sshd on server machine 
3) Run: $ sshuttle -r <USERNAME>@<IP_ADDRESS> 0.0.0.0/0 --dns
```


```
-- OpenVPN
1) Install OpenVPN script
    1.1) example configs in /examples/openvpn_config.txt
2) Modify OpenVPN server’s configuration in /etc/openvpn/server/server.conf
    2.1) Remove all the existing push "dhcp-option DNS x.x.x.x and add push "dhcp-option DNS 10.8.0.1"
3) Restart OpenVPN Services 
    3.1) systemctl daemon-reload
    3.2) systemctl restart openvpn // just restarting openvpn does not change the configuration for OpenVPN server.
    3.3) systemctl restart openvpn-server@server.service
4) Install PiHole script
    4.1) Make sure to select tun0 as interface
    4.2) Select 'No' when prompted to use current networks settings as a static address
    4.3) 10.8.0.1/24 should be the static address OpenVPN will use to talk to PiHole
5) Test DNS script
6) Check http://pi.hole/admin after connecting for live stats
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
-- PiHole
1) sudo vim /etc/pihole/setupVars.conf [IPV4_ADDRESS=10.8.0.1/24]
2) sudo vim /etc/openvpn/server/server.conf [push "dhcp-option DNS 10.8.0.1"]
3) sudo systemctl restart openvpn-server@server
4) sudo echo -e '127.0.0.1\t$(hostname)' >> /etc/hosts
```
