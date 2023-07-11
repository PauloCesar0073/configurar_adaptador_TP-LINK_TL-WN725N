Segue o passo a passo para configurar e ativar seu TP-LINK TL-WN725N:

1. Atualize o sistema:
```bash
sudo apt update
sudo apt upgrade
```

2. Instale o driver necessário:
```bash
sudo apt install realtek-rtl8188eus*
```

3. Adicione o adaptador à lista de blacklist:
```bash
echo 'blacklist r8188eus' | sudo tee -a '/etc/modprobe.d/realtek.conf'
```

4. Configure o NetworkManager:

4.1. Obtenha o endereço MAC do adaptador Wi-Fi:
```bash
ifconfig wlan0 | grep ether
```

4.2. Edite o arquivo `/etc/NetworkManager/NetworkManager.conf`:
```bash
sudo nano /etc/NetworkManager/NetworkManager.conf
```

4.3. Adicione as seguintes linhas ao arquivo:
```
[main]
plugins=ifupdown,keyfile

[device]
wifi.scan-rand-mac-address=no

[ifupdown]
managed=false

[connection]
wifi.powersave=0

[keyfile]
unmanaged-devices=mac:[mac-do-adaptador]
```

Certifique-se de substituir `[mac-do-adaptador]` pelo endereço MAC obtido no passo 4.1.

Após editar o arquivo, salve e feche o editor.



