import os
import subprocess
from time import sleep


def dependencies():
    os.system('sudo apt update')
    os.system('sudo apt upgrade')
    os.system('sudo apt install realtek-rtl8188eus*')
    

    print(30*"=","\n")
    print('\n\n\ndependências instaladas\n')
    print(30*"=","\n")



def add_to_blacklist():
    print('Passo 3: Adicionar o Adaptador à Blacklist\n')
    os.system("echo 'blacklist r8188eus' | sudo tee -a '/etc/modprobe.d/realtek.conf'")


def configure_network_manager():
    print('Passo 4: Configurar o NetworkManager\n')
    print('Passo 4.1. Obter o Endereço MAC do Adaptador Wi-Fi\n')
        # Capturar a saída do comando em uma variável
    mac_output = subprocess.check_output(["ifconfig wlan0 | awk '/ether/ {print $2} /unspec/ {print $2}'"], shell=True, text=True).strip()
    mac_address = mac_output
    cmd = f"[main]\nplugins=ifupdown,keyfile\n[device]\nwifi.scan-rand-mac-address=no\n[ifupdown]\nmanaged=false\n[connection]\nwifi.powersave=0\n[keyfile]\nunmanaged-devices=mac:{mac_output}"

    print('Passo 4.2. Editar o Arquivo NetworkManager.conf\n')
    sleep(2)

    os.system(f'echo "{cmd}" > /etc/NetworkManager/NetworkManager.conf')
    print(30*"=","\n")
    print("configurado ! \n")
    print(30*"=","\n")


def enable_monitor_mode():
    print("Passo 5: Colocar o Adaptador em Modo Monitor:\n")
    mode_choice = input("Deseja tentar em qual modo?\n1.Sim\n2.Não\n")

    if mode_choice == "s":
        print('Usando iwconfig\n')
        os.system('sudo ip link set wlan0 down')
        os.system('sudo iw dev wlan0 set type monitor')
        print(30*"=","\n")
        print("modo monitor ativo !\n\n")
        print(30*"=","\n")
    elif mode_choice == "2":
        os.system("clear")
        print("ok ...coloque manualmente !\n\n")

    else:
        print('Opção inválida! Ative manualmente.')


def main():
    dependencies()
    add_to_blacklist()
    configure_network_manager()
    enable_monitor_mode()
    print(40*"=","\n")
    print("Agora é só realizar um scan. Caso não consiga, reinicie o Kali, coloque a interface em modo monitor e tente novamente um scan\nEX: wifite")
    print(40*"=","\n")


if __name__ == "__main__":
    main()

