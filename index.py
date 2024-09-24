def divisao():
    print("="*50)

saldo_bancario = 0
num_saques = 0
limite_saques = 3
limite = 500.00
extrato = ""

print("Usuário: Caroline")
while True:
    divisao()
    acao = int(input("""[1] Depositar
[2] Sacar
[3] Visualizar saldo e extrato
[4] Sair
Escolha uma das opções de serviço que deseja realizar: """))
    divisao()

    if acao == 1:  # Depositar
        valor_deposito = float(input("Informe o valor do depósito: "))
        
        if valor_deposito > 0:
            saldo_bancario += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"Saldo atual: R$ {saldo_bancario:.2f}")
            
        else:
            print("Não é permitido depositar valores negativos ou nulos.")
        divisao()
            
    elif acao == 2:  # Sacar
        
        if num_saques < limite_saques: 
            valor_saque = float(input("Informe o valor do saque: "))
            
            if valor_saque > limite:
                print("Não é permitido sacar mais de R$500,00 por saque.")
                
            elif valor_saque <= saldo_bancario:
                saldo_bancario -= valor_saque
                num_saques += 1
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
                print(f"Saldo atual: R$ {saldo_bancario:.2f}")
                
            else:
                print("Você não pode sacar um valor maior que seu saldo bancário.")
                
        else:
            print("Você excedeu o número de saques diários (máximo de 3 saques).")
        divisao()

    elif acao == 3:  # Visualizar saldo e extrato
        
        print("\n================ EXTRATO ================")
        
        if not extrato:
            print("Não foram realizadas movimentações.")
            
        else:
            print(extrato)
            
        print(f"\nSaldo: R$ {saldo_bancario:.2f}")
        divisao()

    elif acao == 4:  # Sair
        print("Obrigado pela preferência, volte sempre!")
        break

    else:
        print("Opção inválida, tente novamente.")
