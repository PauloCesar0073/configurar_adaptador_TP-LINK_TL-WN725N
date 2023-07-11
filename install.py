import subprocess

print('Passo 1: Atualizar o Sistema\n')
subprocess.run(['sudo', 'apt', 'update'])
subprocess.run(['sudo', 'apt', 'upgrade'])

print('Passo 2: Instalar o Driver\n')
subprocess.run(['sudo', 'apt', 'install', 'realtek-rtl8188eus*'])

print('Passo 3: Adicionar o Adaptador à Blacklist\n')
subprocess.run(['echo', 'blacklist r8188eus | sudo tee -a /etc/modprobe.d/realtek.conf'], shell=True)

print('Passo 4: Configurar o NetworkManager\n')
print('Passo 4.1. Obter o Endereço MAC do Adaptador Wi-Fi\n')
mac_address = subprocess.run(['ifconfig', 'wlan0', '|', 'awk', "'/ether/ {print $2} /unspec/ {print $2}'"], capture_output=True, text=True).stdout.strip()

print('Passo 4.2. Editar o Arquivo NetworkManager.conf\n')
subprocess.run(['sudo', 'nano', '/etc/NetworkManager/NetworkManager.conf'])

print('Passo 4.3. Adicionar as Configurações ao Arquivo\n')
network_manager_conf = f'''
[main]
plugins=ifupdown,keyfile

[device]
wifi.scan-rand-mac-address=no

[ifupdown]
managed=false

[connection]
wifi.powersave=0

[keyfile]
unmanaged-devices=mac:{mac_address}
'''
with open('/etc/NetworkManager/NetworkManager.conf', 'a') as file:
    file.write(network_manager_conf)

print("Passo 5: Colocar o Adaptador em Modo Monitor:")

a = input("desja tentar em qual modo :\n1.Usando airmon-ng\n2.Usando iwconfig\n")


if a == "1":
    print('Usando airmon-ng')
    subprocess.run(['sudo', 'airmon-ng', 'check', 'kill'])
    subprocess.run(['sudo', 'airmon-ng', 'start', 'wlan0'])


elif a == "2":
    print('Usando iwconfig')
    subprocess.run(['sudo', 'ip', 'link', 'set', 'wlan0', 'down'])
    subprocess.run(['sudo', 'iw', 'dev', 'wlan0', 'set', 'type', 'monitor'])
else:
    print('opção inválida ative manualmente !')

print("a  gora é so Realizar um scan")
