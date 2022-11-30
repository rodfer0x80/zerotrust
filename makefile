.PHONY: iptables_setup
                iptables_setup:
                ext/iptables_setup.sh

.PHONY: user_setup
                user_setup:
                ext/user_setup.sh

.PHONY: macchanger
                macchanger:
                ext/macchanger.py

.PHONY: ufw_setup
                ufw_setup:
                ext/ufw_setup.sh

