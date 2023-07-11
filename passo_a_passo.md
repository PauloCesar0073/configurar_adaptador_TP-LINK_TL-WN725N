# Configurar e Ativar o Adaptador Wi-Fi TP-LINK TL-WN725N - Passo a Passo

Este guia fornece um passo a passo para configurar e ativar o adaptador Wi-Fi TP-LINK TL-WN725N no Kali Linux.

## Requisitos

- Você deve ter acesso de superusuário (root) para executar os comandos.

## Passo 1: Atualizar o Sistema

Atualize o sistema operacional para garantir que você tenha as versões mais recentes dos pacotes e correções de segurança.

```bash
sudo apt update
sudo apt upgrade
```

## Passo 2: Instalar o Driver

Instale o driver necessário para o adaptador Wi-Fi TP-LINK TL-WN725N.

```bash
sudo apt install realtek-rtl8188eus*
```

## Passo 3: Adicionar o Adaptador à Blacklist

Adicione o adaptador à lista de blacklist para evitar que outros drivers sejam carregados.

```bash
echo 'blacklist r8188eus' | sudo tee -a '/etc/modprobe.d/realtek.conf'
```

## Passo 4: Configurar o NetworkManager

4.1. Obtenha o Endereço MAC do Adaptador Wi-Fi

Execute o seguinte comando para obter o endereço MAC do adaptador Wi-Fi:

```bash
ifconfig wlan0 | awk '/ether/ {print $2} /unspec/ {print $2}'

```

Anote o endereço MAC que é exibido.

4.2. Edite o Arquivo NetworkManager.conf

Abra o arquivo `/etc/NetworkManager/NetworkManager.conf` em um editor de texto.

```bash
sudo nano /etc/NetworkManager/NetworkManager.conf
```

4.3. Adicione as Configurações ao Arquivo

Adicione as seguintes linhas ao arquivo `NetworkManager.conf`:

```plaintext
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

Certifique-se de substituir `[mac-do-adaptador]` pelo endereço MAC que você anotou no passo 4.1.

Salve as alterações e feche o editor de texto.

## Passo 5: Colocar o Adaptador em Modo Monitor

5.1. Usando airmon-ng

Você pode colocar o adaptador em modo monitor usando o `airmon-ng` para matar processos e iniciar o modo monitor:

```bash
sudo airmon-ng check kill
sudo airmon-ng start wlan0
```

5.2. Usando iwconfig

Se preferir, você pode colocar o adaptador em modo monitor usando o `iwconfig`:

```bash
sudo ip link set wlan0 down
sudo iw dev wlan0 set type monitor
```

## Passo 6: Realizar um Scan com o Airodump-ng

Agora você pode usar o `airodump-ng` para realizar um scan e visualizar as redes Wi-Fi disponíveis:

```bash
sudo airodump-ng wlan0
```

Observe que o adaptador está em modo monitor e você verá as informações das redes Wi-Fi detectadas.

Certifique-se de usar as opções apropriadas do `airodump-ng` para personalizar o scan de acordo com suas necessidades.

Lembre-se de que o adaptador estará em modo monitor até que você o restaure para o modo normal.

## Conclusão

Seguindo este guia passo a passo, você poderá configurar e ativar o adaptador Wi-Fi TP-LINK TL-WN725N no Linux, colocando-o em modo monitor para realizar scans e interagir com as redes Wi-Fi disponíveis.


