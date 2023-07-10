#!/usr/bin/bash

# Função para exibir uma barra de progresso
progress_bar() {
    local duration=$1
    local progress=0
    local elapsed=0
    local bar_length=40

    while [[ $elapsed -le $duration ]]; do
        ((elapsed++))
        ((progress = elapsed * bar_length / duration))

        if [[ $progress -gt $bar_length ]]; then
            progress=$bar_length
        fi

        printf "\r[%-${bar_length}s] %d%%" "$(printf '#%.0s' $(seq 1 $progress))" "$((progress * 100 / bar_length))"
        sleep 1
    done

    printf "\n"
}

# Função para exibir mensagens formatadas
textplain() {
    echo "//////////===============================//////////"
    echo "$1"
    echo "//////////===============================//////////"
    echo
}

# Função para exibir uma mensagem de erro e sair do script
exit_with_error() {
    echo "Erro: $1"
    exit 1
}

# Verificar se o endereço MAC foi fornecido como argumento
if [ $# -ne 1 ]; then
    exit_with_error "Uso: $0 <endereço MAC>"
fi

mac_address="$1"
config_file="/etc/NetworkManager/NetworkManager.conf"

clear
textplain "Vamos ativar o seu adaptador [TP-LINK TL-WN725N]"
sleep 3

clear
textplain "Atualizando o sistema..."
progress_bar 3

clear
textplain "Realizando upgrade do sistema..."
progress_bar 3

clear
textplain "Instalando o driver para o adaptador Wi-Fi..."
progress_bar 3

clear
textplain "Configurando NetworkManager"
clear

echo "Configurando NetworkManager com o endereço MAC: $mac_address"
clear

if ! sudo grep -q "unmanaged-devices=mac:$mac_address" "$config_file"; then
    sudo sed -i "/\[keyfile\]/a unmanaged-devices=mac:$mac_address" "$config_file"
    
    textplain "Ativando o modo monitor..."
    sleep 1
    airmon-ng check kill
    clear
    ip link set wlan0 down
    clear
    iw dev wlan0 set type monitor
    clear
else
    textplain "O endereço MAC já está configurado como não gerenciado."
fi
clear
textplain "Configuração concluída."
