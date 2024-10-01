import textwrap

# Menu com as opções 
def menu():
    menu = """\n================ MENU ================
[1] Cadastrar usuário
[2] Nova conta 
[3] Listar contas
[4] Depositar
[5] Sacar
[6] Extrato
[7] Visualizar Perfil
[8] Sair
Escolha uma das opções de serviço que deseja realizar: """
    return int(input(textwrap.dedent(menu)))

# Função para depositar
def depositar(conta, valor_deposito):    
    if valor_deposito > 0:
        conta['saldo_bancario'] += valor_deposito
        conta['extrato'] += f"Depósito: \tR$ {valor_deposito:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n--- Operação falhou! O valor informado é inválido. ---")

# Função para sacar
def sacar(conta, valor_saque):
    limite_saques = 3  # Limite de saques por dia
    if conta['numero_saques'] < limite_saques:         
        if valor_saque > 500:
            print("\n--- Não é permitido sacar mais de R$500,00 por saque. ---")
        elif valor_saque <= conta['saldo_bancario']:
            conta['saldo_bancario'] -= valor_saque
            conta['numero_saques'] += 1
            conta['extrato'] += f"Saque: \tR$ {valor_saque:.2f}\n"
            print("\n=== Saque realizado com sucesso! ===")
        else:
            print("\n--- Operação falhou! Você não tem saldo suficiente. ---")
    else:
        print("\n--- Operação falhou! Número máximo de saques excedido. ---")

# Função para exibir extrato
def exibir_extrato(conta):
    print("\n================ EXTRATO ================")
    if not conta['extrato']:
        print("Não foram realizadas movimentações.")
    else:
        print(conta['extrato'])
        print(f"\nSaldo:\t\tR$ {conta['saldo_bancario']:.2f}")
    print("==========================================")

# Função para visualizar perfil do usuário
def visualizar_perfil(usuario):
    print(textwrap.dedent(f"""\n================ PERFIL ================
    Nome: {usuario["nome"]}
    CPF: {usuario["cpf"]}
    Data de Nascimento: {usuario["data_nascimento"]}
    Endereço: {usuario["endereco"]}
    """))

# Função para cadastrar um novo usuário
def cadastrar_usuario(usuarios):
    cpf = input("Informe seu CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n--- Já existe usuário com esse CPF! ---")
        return 
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário cadastrado com sucesso! ===")     

# Função para filtrar usuário pelo CPF
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

# Função para criar nova conta para o usuário
def criar_conta(agencia, numero_conta, usuario):
    return {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario,
        "saldo_bancario": 0,
        "extrato": "",
        "numero_saques": 0
    }

# Função para listar todas as contas
def listar_contas(contas):
    print("\n================ CONTAS ================")
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print(textwrap.dedent(linha))
        print("=" * 40)

# Função principal
def main():
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        if opcao == 1:
            cadastrar_usuario(usuarios)
            
        elif opcao == 2:
            cpf = input("Informe o CPF do usuário: ")
            usuario = filtrar_usuario(cpf, usuarios)

            if usuario:
                numero_conta = len(contas) + 1
                conta = criar_conta(AGENCIA, numero_conta, usuario)
                contas.append(conta)
                print("\n=== Conta criada com sucesso! ===")
            else:
                print("\n--- Usuário não encontrado! ---")

        elif opcao == 3:
            listar_contas(contas)

        elif opcao == 4:
            numero_conta = int(input("Informe o número da conta: ")) - 1
            valor_deposito = float(input("Informe o valor do depósito: "))
            if 0 <= numero_conta < len(contas):
                depositar(contas[numero_conta], valor_deposito)
            else:
                print("\n--- Conta inválida! ---")

        elif opcao == 5:
            numero_conta = int(input("Informe o número da conta: ")) - 1
            valor_saque = float(input("Informe o valor do saque: "))
            if 0 <= numero_conta < len(contas):
                sacar(contas[numero_conta], valor_saque)
            else:
                print("\n--- Conta inválida! ---")

        elif opcao == 6:
            numero_conta = int(input("Informe o número da conta: ")) - 1
            if 0 <= numero_conta < len(contas):
                exibir_extrato(contas[numero_conta])
            else:
                print("\n--- Conta inválida! ---")

        elif opcao == 7:
            cpf = input("Informe o CPF do usuário: ")
            usuario = filtrar_usuario(cpf, usuarios)
            if usuario:
                visualizar_perfil(usuario)
            else:
                print("\n--- Usuário não encontrado! ---")

        elif opcao == 8:
            sair()
            break

# Função para encerrar o programa
def sair():
    print("Obrigado pela preferência, volte sempre!")

main()
