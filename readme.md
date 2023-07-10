# Configurar Adaptador Wi-Fi TP-LINK TL-WN725N - Modo de Uso

Este script automatiza o processo de configuração do adaptador Wi-Fi TP-LINK TL-WN725N no Linux.

## Modo de Uso

1. Baixe o script ou clone o repositório:

   ```bash
   git clone https://github.com/PauloCesar0073/configurar_adaptador_TP-LINK_TL-WN725N
   ```

   ou

   ```bash
   wget https://github.com/PauloCesar0073/configurar_adaptador_TP-LINK_TL-WN725N/blob/main/configurar.sh
   ```

2. Dê permissão de execução ao script:

   ```bash
   chmod +x configurar.sh
   ```

3. Execute o script no terminal, fornecendo o endereço MAC do adaptador Wi-Fi como argumento:

   ```bash
   ./configurar.sh <endereço MAC>
   ```

   Substitua `<endereço MAC>` pelo endereço MAC do adaptador Wi-Fi. Certifique-se de que o adaptador esteja conectado corretamente ao sistema.

4. O script irá realizar as seguintes etapas:

   - Atualizar o sistema
   - Fazer upgrade do sistema
   - Instalar o driver necessário para o adaptador Wi-Fi
   - Configurar o NetworkManager com o endereço MAC fornecido
   - Ativar o modo monitor no adaptador Wi-Fi

5. Siga as instruções fornecidas no terminal durante o processo de configuração.



após estas etapas seu adaptador podera trabalhar em`(modo monitor)` e você poderar usar corretamente ferramentas que necessitam de uma interface em modo monitor.

## Requisitos

- Este script é destinado ao uso no Kali Linux versão do kernel `6.3.0-kali1-amd64`
(não testei em outras distros ou versões anteriores..)
- É necessário ter privilégios de superusuário para executar o script.
- Certifique-se de ter uma conexão de internet ativa para que o script possa atualizar e fazer upgrade do sistema, se necessário.


<hr>
espero que o ajude ! assim como me ajudou .
