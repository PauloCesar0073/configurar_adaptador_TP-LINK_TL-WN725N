#!/bin/bash

# Função para exibir mensagens formatadas
textplain() {
    echo "==============================="
    echo "$1"
    echo "==============================="
    echo
}

# Função para exibir uma mensagem de erro e sair do script
exit_with_error() {
    echo "Erro: $1"
    exit 1
}

# Verificar se o usuário tem privilégios de superusuário
if [[ $EUID -ne 0 ]]; then
    exit_with_error "Este script deve ser executado com privilégios de superusuário."
fi

# Atualizar o sistema
textplain "Atualizando o sistema..."
if ! apt update; then
    exit_with_error "Falha ao atualizar o sistema."
fi

# Fazer upgrade do sistema
textplain "Realizando upgrade do sistema..."
if ! apt upgrade -y; then
    exit_with_error "Falha ao realizar upgrade do sistema."
fi

# Instalar o driver necessário
textplain "Instalando o driver para o adaptador Wi-Fi..."
if ! apt install -y realtek-rtl8188eus*; then
    exit_with_error "Falha ao instalar o driver necessário."
fi

# Adicionar o adaptador à lista de blacklist
textplain "Adicionando o adaptador à lista de blacklist..."
if ! echo 'blacklist r8188eus' | sudo tee -a '/etc/modprobe.d/realtek.conf'; then
    exit_with_error "Falha ao adicionar o adaptador à lista de blacklist."
fi

# Obter o endereço MAC do adaptador Wi-Fi
textplain "Obtendo o endereço MAC do adaptador Wi-Fi..."
mac_address=$(ifconfig wlan0 | awk '/ether/ {print $2}')
if [[ -z $mac_address ]]; then
    exit_with_error "Falha ao obter o endereço MAC do adaptador Wi-Fi."
fi

# Configurar o NetworkManager
textplain "Configurando o NetworkManager..."
config_file="/etc/NetworkManager/NetworkManager.conf"

# Verificar se o endereço MAC já está configurado como não gerenciado
if grep -q "unmanaged-devices=mac:$mac_address" "$config_file"; then
    textplain "O endereço MAC já está configurado como não gerenciado."
    exit 0
fi

# Adicionar o endereço MAC à configuração do NetworkManager
if ! sudo sed -i "/\[keyfile\]/a unmanaged-devices=mac:$mac_address" "$config_file"; then
    exit_with_error "Falha ao adicionar o endereço MAC à configuração do NetworkManager."
fi

textplain "Configuração concluída."
echo "Finalizado!"
