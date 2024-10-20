# Desafio 1: Sistema Bancário

Este repositório contém o código desenvolvido para o bootcamp **NTT DATA - Engenharia de Dados com Python** da plataforma de ensino **Digital Innovation One (DIO)**.

O objetivo deste projeto é criar um sistema bancário simples com as seguintes funcionalidades:

- Cadastro de usuários
- Criação de contas bancárias
- Depósito
- Saque (com limite de valor por saque e número de saques diários)
- Visualização de extrato
- Limite de 3 saques diários
- Saque máximo de R$500,00 por operação
- Visualização de perfil do usuário

## Funcionalidades

1. **Cadastrar Usuário**: Permite o cadastro de um novo usuário com informações como nome, CPF, data de nascimento e endereço.
2. **Criar Conta**: Associa uma nova conta bancária a um usuário já cadastrado.
3. **Depositar**: Permite ao usuário depositar um valor positivo na conta bancária.
4. **Sacar**: O usuário pode realizar saques com um limite de 3 saques diários e até R$500,00 por saque.
5. **Visualizar extrato**: Exibe o saldo atual e um extrato das operações realizadas (depósitos e saques).
6. **Visualizar Perfil**: Mostra as informações do perfil do usuário cadastrado.
7. **Sair**: Encerra o sistema bancário.

## Otimizações Implementadas

- **Separação de funcionalidades**: As funções foram organizadas de maneira a melhorar a legibilidade e facilitar a manutenção do código.
- **Controle de Acesso**: O sistema garante que cada usuário só possa depositar e sacar de sua própria conta, evitando interações indesejadas entre diferentes contas.
- **Feedback ao Usuário**: Mensagens de sucesso e erro foram implementadas para melhorar a experiência do usuário.

## Requisitos

- Python 3.x instalado

## Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
2. Acesse a pasta do projeto:
   ```bash
   cd seu-repositorio
3. Execute o arquivo Python:
   ```bash
   python nome_do_arquivo.py
