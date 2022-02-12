#!/bin/bash
while [ 1 ]
do
	echo -e "\n\n***********************"
	echo "    vpn manager"
	echo -e "\n***********************"
	echo "0) Exit"
	echo "1) Start"
	echo "2) Stop"
	echo "3) Restart"
	echo "4) Status"
	read -p ">>> " c
	[ "$c" == 0 ] && exit
	[ "$c" == 1 ] && sudo systemctl start openvpn-server@server.service && echo -e "\n[INFO] Connection started."
	[ "$c" == 2 ] && sudo systemctl stop openvpn-server@server.service && echo -e "\n[INFO] Connection stopped."
	[ "$c" == 3 ] && sudo systemctl restart openvpn-server@server.service && echo -e "\n[INFO] Connection restarted."
	[ "$c" == 4 ] && sudo systemctl status openvpn-server@server.service
done
