# Desafios e Aprendizados do Bootcamp Suzano com Python
## Desafio Sistema Bancario com Python

- Este é um sistema bancário simples, desenvolvido em Python, que permite aos usuários realizar operações básicas como depósito, saque e verificação de extrato. O sistema é executado via console e simula as funcionalidades essenciais de uma conta bancária.

### Como Usar
Para executar este sistema, você precisará ter o Python instalado em sua máquina.

Salve o código: Copie o código-fonte fornecido e salve-o em um arquivo com extensão .py (por exemplo, banco.py).

Execute via terminal: Abra um terminal ou prompt de comando, navegue até o diretório onde você salvou o arquivo e execute o comando:

python banco.py

Interaja com o menu: O sistema apresentará um menu de opções. Digite a letra correspondente à operação desejada e pressione Enter.

[s] sacar
[d] depositar
[e] extrato
[q] sair

### Funcionalidades
Depósito (d):

Permite depositar valores positivos na conta.

Atualiza o saldo e registra a transação no extrato.

Saque (s):

Permite sacar dinheiro da conta.

Limites:

Cada saque é limitado a R$ 500,00.

O número máximo de saques diários é 3.

Verifica se há saldo suficiente e se os limites foram excedidos.

Atualiza o saldo e registra a transação no extrato.

Extrato (e):

Exibe todas as movimentações (depósitos e saques) realizadas na conta.

Informa o saldo atual.

Caso não haja movimentações, exibe uma mensagem indicando.

Sair (q):

Encerra o sistema.