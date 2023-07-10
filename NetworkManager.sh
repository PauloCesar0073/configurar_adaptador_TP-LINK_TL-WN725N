#!/bin/bash
echo "Configurando NetworkManager"
if [ $# -ne 1 ]; then
    echo "Uso: $0 <endereço MAC>"
    exit 1
fi

mac_address="$1"
config_file="/etc/NetworkManager/NetworkManager.conf"

echo "Configurando NetworkManager com o endereço MAC: $mac_address"

if ! sudo grep -q "unmanaged-devices=mac:$mac_address" "$config_file"; then
    sudo sed -i "/\[keyfile\]/a unmanaged-devices=mac:$mac_address" "$config_file"
    echo "Configuração concluída."
else
    echo "O endereço MAC já está configurado como não gerenciado."
fi
