.PHONY: test_dns
test_dns:
	ext/test_dns.sh

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

.PHONY: openvpn-install
openvpn-install:
	scripts/openvpn-install.sh

.PHONY: hw_pivpn_install
hw_pivpn_install:
	scripts/hw_pivpn_install.sh

