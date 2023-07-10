#!/bin/bash

clear
echo "Vamos ativar o seu adaptador [TP-LINK TL-WN725N]"

sleep 3

apt update -y

clear
apt upgrade -y

clear
apt install realtek-rtl8188eus

clear
printf 'blacklist r8188eus' | sudo tee -a '/etc/modprobe.d/realtek.conf'

clear

if [ $# -ne 1 ]; then
    echo "Uso: $0 <endereço MAC>"
    exit 1
fi

mac_address="$1"
config_file="/etc/NetworkManager/NetworkManager.conf"

echo "Configurando NetworkManager com o endereço MAC: $mac_address"

if ! sudo grep -q "unmanaged-devices=mac:$mac_address" "$config_file"; then
    sudo sed -i "/\[keyfile\]/a unmanaged-devices=mac:$mac_address" "$config_file"
	
	echo "Ativando o modo monitor...."
	sleep 1
	airmon-ng check kill
	clear
	ip link set wlan0 down
	clear
	iw dev wlan0 set type monitor
	clear
    echo "Configuração concluída."
else
    echo "O endereço MAC já está configurado como não gerenciado."
fi

echo "Finalizado!"
