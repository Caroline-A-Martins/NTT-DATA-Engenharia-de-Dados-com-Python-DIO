from abc import ABC, ABCMeta, abstractmethod
from datetime import datetime
import textwrap

# Classe Cliente - Define um cliente genérico com um endereço e contas associadas
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []  # Lista de contas associadas ao cliente
    
    # Método para realizar uma transação em uma conta específica
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    # Método para adicionar uma nova conta ao cliente
    def adicionar_conta(self, conta):
        self.contas.append(conta)

# Classe PessoaFisica - Subclasse de Cliente, específica para pessoas físicas
class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

# Classe Conta - Representa uma conta bancária genérica
class Conta:
    def __init__(self, numero, cliente):
        self.saldo = 0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = Historico()  # Instância de um objeto Historico para registrar as transações
    
    # Método para criar uma nova conta
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    # Propriedades para acessar os atributos da conta
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._clenete
    
    @property
    def historico(self):
        return self._historico
    
    # Método para sacar dinheiro da conta
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo
        
        if excedeu_saldo:
            print("\n--- Operação falhou! Você não tem saldo suficiente. ---")
        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True
        else:
            print("\n--- Operação falhou! O valor informado é inválido ---")
        
        return False

    # Método para depositar dinheiro na conta
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n--- Operação falhou! Valor inválido. ---")
            return False
        return True

# Classe ContaCorrente - Subclasse de Conta com limites de saque
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saque=3):
        super().__init__(numero, cliente)
        self.limite = limite  # Limite de saque diário
        self.limite_saque = limite_saque  # Limite de saques diários
    
    # Método para sacar levando em conta os limites de saque
    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])
        
        excedeu_limite = valor > self.limite
        excedeu_saque = numero_saques >= self.limite_saque
        
        if excedeu_limite:
            print("\n--- Operação falhou! O valor do saque excedeu o limite. ---")
        elif excedeu_saque:
            print("\n--- Operação falhou! Número máximo de saques excedido. ---")
        else:
            return super().sacar(valor)
    
    # Método para exibir os dados da conta ao ser impressa
    def __str__(self):
        return f"""\nAgência:\t{self.agencia}\nC/C:\t\t{self.numero}\nTitular:\t{self.cliente.nome}"""

# Classe Historico - Mantém o registro das transações realizadas
class Historico:
    def __init__(self):
        self.transacoes = []  # Lista de transações
    
    # Propriedade para acessar as transações
    @property
    def transacoes(self):
        return self._transacoes
    
    # Método para adicionar uma transação ao histórico
    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
        })

# Classe abstrata Transacao - Define o contrato para diferentes tipos de transações
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass
    
    @abstractmethod
    def registrar(self, conta):
        pass

# Classe Saque - Representa a transação de saque
class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor
    
    @property
    def valor(self):
        return self.valor
    
    # Método para registrar o saque em uma conta
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

# Classe Deposito - Representa a transação de depósito
class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor
    
    @property
    def valor(self):
        return self.valor
    
    # Método para registrar o depósito em uma conta
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

# Menu - Função que exibe as opções disponíveis
def menu():
    menu = """\n================ MENU ================\n[1] Criar usuário\n[2] Nova conta\n[3] Listar contas\n[4] Depositar\n[5] Sacar\n[6] Extrato\n[7] Visualizar Perfil\n[8] Sair\nEscolha uma das opções de serviço que deseja realizar: """
    return int(input(textwrap.dedent(menu)))

# Função para filtrar clientes pelo CPF
def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

# Função para recuperar a conta de um cliente
def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n--- Cliente não possui conta! ---")
        return None
    return cliente.contas[0]

# Função para depositar dinheiro na conta de um cliente
def depositar(clientes):
    cpf = input("Informe o CPF do usuário: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print("\n--- Operação falhou! Cliente não encontrado. ---")
        return
    
    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)
    
    conta = recuperar_conta_cliente(cliente)
    if conta:
        cliente.realizar_transacao(conta, transacao)

# Função para sacar dinheiro da conta de um cliente
def sacar(clientes):
    cpf = input("Informe o CPF do usuário: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print("\n--- Operação falhou! Cliente não encontrado. ---")
        return
    
    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)
    
    conta = recuperar_conta_cliente(cliente)
    if conta:
        cliente.realizar_transacao(conta, transacao)

# Função para exibir o extrato de uma conta
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
    transacoes = conta.historico.transacoes
    extrato = ""
    
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"
    
    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")

# Função para visualizar o perfil de um cliente
def visualizar_perfil(clientes):
    cpf = input("Informe o CPF do usuário: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print("\n--- Operação falhou! Cliente não encontrado. ---")
        return
    
    print(textwrap.dedent(f"""\n================ PERFIL ================\nNome: {cliente.nome}\nCPF: {cliente.cpf}\nData de Nascimento: {cliente.data_nascimento}\nEndereço: {cliente.endereco}\n"""))

# Função para criar um novo cliente
def criar_cliente(clientes):
    cpf = input("Informe seu CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n--- Já existe usuário com esse CPF! ---")
        return 
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(cliente)
    
    print("\n=== Usuário cadastrado com sucesso! ===")

# Função para criar uma nova conta para um cliente existente
def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do usuário: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print("\n--- Operação falhou! Cliente não encontrado, fluxo de criação de conta encerrado! ---")
        return
    
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)
    
    print("\n=== Conta criada com sucesso! ===")

# Função para listar todas as contas
def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))

# Função principal que controla o fluxo do programa
def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()
        
        if opcao == 1:
            criar_cliente(clientes)
        
        if opcao == 2:
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        if opcao == 3:
            listar_contas(contas)

        if opcao == 4:
            depositar(clientes)

        elif opcao == 5:
            sacar(clientes)

        elif opcao == 6:
            exibir_extrato(clientes)
        
        elif opcao == 7:
            visualizar_perfil(clientes)
        
        elif opcao == 8:
            sair()
            break

# Função para encerrar o programa
def sair():
    print("Obrigado pela preferência, volte sempre!")

main()
