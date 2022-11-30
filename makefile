.PHONY: iptables_setup
iptables_setup:
	ext/iptables_setup.sh

.PHONY: user_setup
user_setup:
	ext/user_setup.sh

.PHONY: macchanger
macchanger:
	ext/macchanger.py

.PHONY: pihole_install
pihole_install:
	scripts/pihole_install.sh

.PHONY: openvpn_install
openvpn_install:
	scripts/openvpn_install.sh

.PHONY: hw_pivpn_install
hw_pivpn_install:
	scripts/hw_pivpn_install.sh

