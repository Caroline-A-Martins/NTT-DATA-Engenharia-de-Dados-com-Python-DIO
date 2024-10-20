from datetime import datetime
import textwrap

# Função para criar um cliente
def criar_cliente(clientes):
    cpf = input("Informe seu CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n--- Já existe usuário com esse CPF! ---")
        return 

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = {
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "endereco": endereco,
        "contas": []
    }
    
    clientes.append(cliente)
    print("\n=== Usuário cadastrado com sucesso! ===")

# Função para criar uma nova conta para um cliente
def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do usuário: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print("\n--- Operação falhou! Cliente não encontrado! ---")
        return
    
    conta = {
        "numero": numero_conta,
        "agencia": "0001",
        "cliente": cliente,
        "saldo": 0,
        "limite": 500,
        "limite_saque": 3,
        "historico": []
    }

    contas.append(conta)
    cliente["contas"].append(conta)
    print("\n=== Conta criada com sucesso! ===")

# Função para filtrar cliente pelo CPF
def filtrar_cliente(cpf, clientes):
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            return cliente
    return None

# Função para recuperar a conta de um cliente
def recuperar_conta_cliente(cliente):
    if not cliente["contas"]:
        print("\n--- Cliente não possui conta! ---")
        return None
    return cliente["contas"][0]

# Função para realizar depósito
def depositar(clientes):
    cpf = input("Informe o CPF do usuário: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print("\n--- Operação falhou! Cliente não encontrado. ---")
        return

    valor = float(input("Informe o valor do depósito: "))
    conta = recuperar_conta_cliente(cliente)

    if conta and valor > 0:
        conta["saldo"] += valor
        conta["historico"].append({
            "tipo": "Depósito",
            "valor": valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        })
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n--- Operação falhou! Valor inválido ou conta não encontrada. ---")

# Função para realizar saque
def sacar(clientes):
    cpf = input("Informe o CPF do usuário: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n--- Operação falhou! Cliente não encontrado. ---")
        return

    valor = float(input("Informe o valor do saque: "))
    conta = recuperar_conta_cliente(cliente)

    if conta:
        numero_saques = len([transacao for transacao in conta["historico"] if transacao["tipo"] == "Saque"])

        if valor > conta["saldo"]:
            print("\n--- Operação falhou! Saldo insuficiente. ---")
        elif numero_saques >= conta["limite_saque"]:
            print("\n--- Operação falhou! Limite de saques excedido. ---")
        else:
            conta["saldo"] -= valor
            conta["historico"].append({
                "tipo": "Saque",
                "valor": valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            })
            print("\n=== Saque realizado com sucesso! ===")

# Função para exibir o extrato
def exibir_extrato(clientes):
    cpf = input("Informe o CPF do usuário: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n--- Operação falhou! Cliente não encontrado. ---")
        return

    conta = recuperar_conta_cliente(cliente)

    if not conta:
        return

    print("\n================ EXTRATO ================")
    if not conta["historico"]:
        print("Não foram realizadas movimentações.")
    else:
        for transacao in conta["historico"]:
            print(f"{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}")
    
    print(f"\nSaldo:\n\tR$ {conta['saldo']:.2f}")
    print("==========================================")

# Função para visualizar o perfil do cliente
def visualizar_perfil(clientes):
    cpf = input("Informe o CPF do usuário: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n--- Operação falhou! Cliente não encontrado. ---")
        return

    print(f"\n================ PERFIL ================\nNome: {cliente['nome']}\nCPF: {cliente['cpf']}\nData de Nascimento: {cliente['data_nascimento']}\nEndereço: {cliente['endereco']}\n")

# Função para listar contas
def listar_contas(contas):
    for conta in contas:
        print("=" * 40)
        print(f"Agência: {conta['agencia']}\nConta: {conta['numero']}\nTitular: {conta['cliente']['nome']}")

# Menu do sistema
def menu():
    opcoes = """\n================ MENU ================\n[1] Criar usuário\n[2] Nova conta\n[3] Listar contas\n[4] Depositar\n[5] Sacar\n[6] Extrato\n[7] Visualizar Perfil\n[8] Sair\nEscolha uma opção: """
    return int(input(textwrap.dedent(opcoes)))

# Função principal
def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 1:
            criar_cliente(clientes)
        elif opcao == 2:
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        elif opcao == 3:
            listar_contas(contas)
        elif opcao == 4:
            depositar(clientes)
        elif opcao == 5:
            sacar(clientes)
        elif opcao == 6:
            exibir_extrato(clientes)
        elif opcao == 7:
            visualizar_perfil(clientes)
        elif opcao == 8:
            print("Obrigado pela preferência, volte sempre!")
            break

# Início do programa
main()
