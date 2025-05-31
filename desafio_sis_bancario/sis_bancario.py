menu = """
[s] sacar
[d] depositar
[e] extrato
[q] sair

"""
saldo = 0
limite = 500
extrato = ""
num_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    match opcao:
        case 'd':
            valor = float(input('Informe o valor do deposito: '))

            if valor > 0:
                saldo += valor
                extrato == f'Depósito R${valor:.2f}\n'
            else:
                print('Valor Informado é Invalido')
        case 's':
            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > saldo
            excedeu_limit = valor > limite
            excedeu_saques = num_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Voce não tem saldo suficiente")
            elif excedeu_limit:
                print("Valor de saque excedeu o limite")  
            elif excedeu_saques:
                print("Numero maximo de saques excedidos")  
            elif valor > 0:
                saldo -= valor
                extrato == f"Saque: R$ {valor:.2f}\n"
                num_saques += 1
            else:
                print('Valor informado é invalido')
        case 'e':
            print('\n################# EXTRATO ##################')
            print('Não foram realizadas movimentações' if not extrato else extrato)
            print('\n Saldo: R$ {saldo:.2f}')
            print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')

        case 'q':
            break     

        case _:
            print("Operação inválida!")        

