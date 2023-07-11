# Configurando o Adaptador Wi-Fi TP-LINK TL-WN725N no Kali Linux

Se você possui o adaptador Wi-Fi TP-LINK TL-WN725N e deseja configurá-lo no Kali Linux, existem duas opções disponíveis:

1. **Configuração Manual (Passo a Passo):**
   Se você preferir configurar manualmente, siga o [passo a passo](passo_a_passo) fornecido.

2. **Script de Automação:**
   Você também pode usar um script que automatiza o processo de configuração. Execute os seguintes comandos no terminal:

```bash
git clone https://github.com/PauloCesar0073/configurar_adaptador_TP-LINK_TL-WN725N &&
cd configurar_adaptador_TP-LINK_TL-WN725N &&
chmod +x install.sh &&
clear &&
./install.sh
```

**Observações:**
- recomendo o passo a passo pois o script automatizado pode deixar passar erros !

- Certifique-se de que o adaptador esteja ativo no seu Kali Linux. Verifique digitando `lsusb` no terminal.

- A versão do kernel testada foi `6.3.0-kali1-amd64`. Se você estiver usando uma versão diferente, pode haver erros.

