#!/bin/bash
clear
echo "Instalando o seu adaptador [TP-LINK TL-WN725N]"

sleep 2

apt update -y

clear
apt upgrade -y

clear
apt install realtek-rtl8188eus* -y


printf 'blacklist r8188eus' | sudo tee -a '/etc/modprobe.d/realtek.conf'

echo "agora execute o proximo script configNetworkManager.sh"


