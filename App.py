import os
from datetime import datetime

class Cliente:
    def __init__(self, nome, cpf, endereco, telefone):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone

    def __str__(self):
        return f"Nome: {self.nome}\nCPF: {self.cpf}\nEndereço: {self.endereco}\nTelefone: {self.telefone}\n"

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return f"Nome: {self.nome}\nPreço: {self.preco}\nQuantidade: {self.quantidade}\n"

class Servico:
    def __init__(self, descricao, preco):
        self.descricao = descricao
        self.preco = preco

    def __str__(self):
        return f"Descrição: {self.descricao}\nPreço: {self.preco}\n"

def cadastrar_cliente():
    nome = input("Informe o nome do cliente: ")
    cpf = input("Informe o CPF do cliente: ")
    endereco = input("Endereço para cadastro: ")
    telefone = input("Telefone para contato: ")

    # Checar se o cliente já está cadastrado
    if cliente_ja_cadastrado(cpf):
        print("Cliente já cadastrado!")
        return None

    novo_cliente = Cliente(nome, cpf, endereco, telefone)
    salvar_cliente(novo_cliente)
    print("Cliente cadastrado com sucesso!")
    return novo_cliente

def cadastrar_produto():
    nome = input("Informe o nome do produto: ")
    preco = float(input("Informe o preço do produto: "))
    quantidade = int(input("Informe a quantidade em estoque: "))

    novo_produto = Produto(nome, preco, quantidade)
    salvar_produto(novo_produto)
    print("Produto cadastrado com sucesso!")
    return novo_produto

def cadastrar_servico():
    descricao = input("Informe a descrição do serviço: ")
    preco = float(input("Informe o preço do serviço: "))

    novo_servico = Servico(descricao, preco)
    salvar_servico(novo_servico)
    print("Serviço cadastrado com sucesso!")
    return novo_servico

def salvar_cliente(cliente):
    with open("clientes.txt", 'a') as arquivo:
        arquivo.write(f"{cliente.nome},{cliente.cpf},{cliente.endereco},{cliente.telefone}\n")

def salvar_produto(produto):
    with open("produtos.txt", 'a') as arquivo:
        arquivo.write(f"{produto.nome},{produto.preco},{produto.quantidade}\n")

def salvar_servico(servico):
    with open("servicos.txt", 'a') as arquivo:
        arquivo.write(f"{servico.descricao},{servico.preco}\n")

def cliente_ja_cadastrado(cpf):
    with open("clientes.txt", 'r') as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(',')
            if dados[1] == cpf:
                return True
    return False

def menu():
    opcao = 0
    while opcao != 5:
        print("\nEscolha uma opção:")
        print("1 - Cadastrar cliente")
        print("2 - Cadastrar produto")
        print("3 - Cadastrar serviço")
        print("4 - Agendar serviço")
        print("5 - Sair")

        opcao = int(input())
        
        if opcao == 1:
            cadastrar_cliente()
        elif opcao == 2:
            cadastrar_produto()
        elif opcao == 3:
            cadastrar_servico()
        elif opcao == 4:
            agendar_servico()
        elif opcao == 5:
            print("Saindo do sistema.")
        else:
            print("Opção inválida. Tente novamente.")

def agendar_servico():
    print("\nAgendar serviço:")
    cpf_cliente = input("Informe o CPF do cliente: ")

    if not cliente_ja_cadastrado(cpf_cliente):
        print("Cliente não encontrado. Cadastre o cliente antes de agendar um serviço.")
        return

    print("Lista de Serviços:")
    mostrar_servicos()

    opcao_servico = int(input("Escolha o número do serviço desejado: "))
    servico = carregar_servico_por_indice(opcao_servico)

    data_agendamento = input("Informe a data do agendamento (DD/MM/YYYY): ")
    try:
        data_formatada = datetime.strptime(data_agendamento, "%d/%m/%Y").date()
    except ValueError:
        print("Formato de data inválido. Use o formato DD/MM/YYYY.")
        return

    print("Serviço agendado com sucesso!")
    print(f"Cliente: {cpf_cliente}")
    print(f"Serviço: {servico}")
    print(f"Data do Agendamento: {data_formatada}")

def mostrar_servicos():
    servicos = carregar_servicos()
    for i, servico in enumerate(servicos, 1):
        print(f"{i} - {servico}")

def carregar_servicos():
    servicos = []
    with open("servicos.txt", 'r') as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(',')
            descricao = dados[0]
            preco = float(dados[1])
            servico = Servico(descricao, preco)
            servicos.append(servico)
    return servicos

def carregar_servico_por_indice(indice):
    servicos = carregar_servicos()
    if 1 <= indice <= len(servicos):
        return servicos[indice - 1]
    else:
        print("Índice inválido.")
        return None

if __name__ == "__main__":
    if not os.path.exists("clientes.txt"):
        open("clientes.txt", 'w').close()

    if not os.path.exists("produtos.txt"):
        open("produtos.txt", 'w').close()

    if not os.path.exists("servicos.txt"):
        open("servicos.txt", 'w').close()

    menu()
