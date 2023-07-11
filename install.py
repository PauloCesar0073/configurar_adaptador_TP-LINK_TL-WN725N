import subprocess
import configparser

def run_command(command):
    subprocess.run(command, shell=True)

def update_system():
    print('Passo 1: Atualizar o Sistema\n')
    run_command(['sudo', 'apt', 'update'])
    run_command(['sudo', 'apt', 'upgrade'])

def install_driver():
    print('Passo 2: Instalar o Driver\n')
    run_command(['sudo', 'apt', 'install', 'realtek-rtl8188eus*'])

def add_to_blacklist():
    print('Passo 3: Adicionar o Adaptador à Blacklist\n')
    run_command("echo 'blacklist r8188eus' | sudo tee -a '/etc/modprobe.d/realtek.conf'")

def configure_network_manager():
    print('Passo 4: Configurar o NetworkManager\n')
    print('Passo 4.1. Obter o Endereço MAC do Adaptador Wi-Fi\n')
    mac_address = subprocess.run(['ifconfig', 'wlan0', '|', 'awk', "'/ether/ {print $2} /unspec/ {print $2}'"], capture_output=True, text=True).stdout.strip()

    print('Passo 4.2. Editar o Arquivo NetworkManager.conf\n')
    config = configparser.ConfigParser()
    config.read('/etc/NetworkManager/NetworkManager.conf')

    if 'keyfile' not in config.sections():
        config['keyfile'] = {}
    
    config['keyfile']['unmanaged-devices'] = f'mac:{mac_address}'

    with open('/etc/NetworkManager/NetworkManager.conf', 'w') as configfile:
        config.write(configfile)

def enable_monitor_mode():
    print("Passo 5: Colocar o Adaptador em Modo Monitor:\n")
    mode_choice = input("Deseja tentar em qual modo?\n1. Usando airmon-ng\n2. Usando iwconfig\n")

    if mode_choice == "1":
        print('Usando airmon-ng\n')
        run_command(['sudo', 'airmon-ng', 'check', 'kill'])
        run_command(['sudo', 'airmon-ng', 'start', 'wlan0'])

    elif mode_choice == "2":
        print('Usando iwconfig\n')
        run_command(['sudo', 'ip', 'link', 'set', 'wlan0', 'down'])
        run_command(['sudo', 'iw', 'dev', 'wlan0', 'set', 'type', 'monitor'])

    else:
        print('Opção inválida! Ative manualmente.')

def main():
    update_system()
    install_driver()
    add_to_blacklist()
    configure_network_manager()
    enable_monitor_mode()

    print("Agora é só realizar um scan. Caso não consiga, reinicie o Kali e coloque a interface em modo monitor e tente novamente um scan")

if __name__ == "__main__":
    main()
